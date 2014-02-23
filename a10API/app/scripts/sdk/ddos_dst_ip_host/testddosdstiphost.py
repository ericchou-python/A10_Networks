#!/usr/bin/env python

import ddos_dst_ip_host
from sdk_auth import *
from ddos_dst_ip_host import *
import httplib, socket, ssl

hostIp = '192.168.1.202'

# patch httplib.HTTPSConnection.connect
def connect_patched(self):
    "Connect to a host on a given (SSL) port."

    sock = socket.create_connection((self.host, self.port),self.timeout, self.source_address)
    if self._tunnel_host:
        self.sock = sock
        self._tunnel()
    self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_TLSv1)

httplib.HTTPSConnection.connect = connect_patched


# Create Authorization Client to get the signature
authClient = AuthorizationClient(endpoint='https://' + hostIp + '/auth', debug=True)
credentials = Credentials(username="admin", password="a10")
authResponse = authClient.submitCredentials(credentials)
signature = authResponse.signature


allDdosDstIpHostsClient = AllDdosDstipHostsClient(endpoint='https://' + hostIp + '/axapi/v3/ddos/dst-ip/host', sessionid=signature, debug=True)
ddosDstipHostClient = DdosDstipHostClient(endpoint='https://' + hostIp + '/axapi/v3/ddos/dst-ip/host', sessionid=signature, debug=True)


# Remove any configuration that already exists for ddos dst-ip host 1.1.1.1
try:
    host = Host_ip_addr('1.1.1.1')
    ddosDstipHostClient.deleteDdosDstipHost(host)
except ddos_dst_ip_host.RemoteException as rex:
        print "status=%s" %rex.status
        print "message=%s" %rex.message
        print "details=%s" %rex.details


# Simple POST example. Apply deny for port 80 tcp for dst-ip host 1.1.1.1
#ddos dst-ip host 1.1.1.1
#  port 80 tcp
#    deny

port80 = Ddos_dst_ip_host_port(port_num= 80, protocol='tcp', deny=1)
port90 = Ddos_dst_ip_host_port(port_num= 90, protocol='tcp', deny=1)

ipProto80 = Ddos_dst_ip_host_ip_proto(port_num=80, deny=0)
ipProto90 = Ddos_dst_ip_host_ip_proto(port_num=90, deny=1)
exceedAction = Ddos_dst_ip_host_l4_type_exceed_action(exceed_drop=1)
classList = Ddos_dst_ip_host_l4_type_class_list(check_all_class_list='all')
scanningDetection = Ddos_dst_ip_host_l4_type_scanning_detection(threshold=31)

l4Type1 = Ddos_dst_ip_host_l4_type(protocol='tcp', \
                                   max_rexmit_syn_per_flow=7, \
                                   exceed_action=exceedAction, \
                                   syn_cookie=1, \
                                   class_list=classList, \
                                   tcp_reset_client=1, \
                                   tcp_reset_server=1)

hostObject = Host(ip_addr='1.1.1.1', portList=[port80, port90], \
                  ip_protoList=[ipProto80, ipProto90], \
                  l4_typeList=[l4Type1], \
                  enable_512_port=1)

try:
    allDdosDstIpHostsClient.submitDdosDstipHost(hostObject)
except ddos_dst_ip_host.RemoteException as rex:
        print "status=%s" %rex.status
        print "message=%s" %rex.message
        print "details=%s" %rex.details

# Fetch an object of type ddos dst-ip host with ip "1.1.1.1"
# sample CLI to apply first
#ddos dst-ip host 1.1.1.1
#  port 80 tcp
#    deny

host = Host_ip_addr('1.1.1.1')
try:
    hostIpObject = ddosDstipHostClient.getDdosDstipHost(host)
    print "Ip-Address=%s" %hostIpObject.ip_addr
    if hostIpObject.portList:
        for port in hostIpObject.portList:
            print "Port Number=%s" %port.port_num
            print "Protocol=%s" %port.protocol
except ddos_dst_ip_host.RemoteException as rex:
        print "status=%s" %rex.status
        print "message=%s" %rex.message
        print "details=%s" %rex.details


