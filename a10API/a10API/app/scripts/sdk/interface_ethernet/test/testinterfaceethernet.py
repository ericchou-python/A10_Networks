#!/usr/bin/python
import interface_ethernet
from interface_ethernet import *
from sdk_auth import *
import httplib, socket, ssl

"""
# patch httplib.HTTPSConnection.connect
def connect_patched(self):
    "Connect to a host on a given (SSL) port."

    sock = socket.create_connection((self.host, self.port),self.timeout, self.source_address)
    if self._tunnel_host:
        self.sock = sock
        self._tunnel()
    self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_TLSv1)

httplib.HTTPSConnection.connect = connect_patched
"""

if __name__ == '__main__':

    hostIp = '10.3.150.184'

    # Retrieve signature using AuthorizationClient
    authClient = AuthorizationClient(endpoint='https://' + hostIp + '/auth',debug=True)
    credentials = Credentials(username="admin", password="a10")
    auth_response = authClient.submitCredentials(credentials)
    print("description",auth_response.description)
    print("signature",auth_response.signature)
    signature = auth_response.signature


    ########## Creating a new ethernet interface

    endpoint = 'https://' + hostIp + '/axapi/v3/interface/ethernet'
    # For convenience we have two types of Https clients

    # All Ethernets Client
    allEthernetsClient = AllInterfaceEthernetsClient(endpoint=endpoint, sessionid=signature, debug=True)
    # Ethernet Id Client
    ethernetIdClient = InterfaceEthernetClient(endpoint=endpoint, sessionid=signature, debug=True)


    # Remove any configuration if it already exists on ethernet 7

    try :
        ethernetIdClient.deleteInterfaceEthernet(Ethernet_ifnum(7))
    except interface_ethernet.RemoteException as rex:
        print "status=%s" %rex.status
        print "message=%s" %rex.message
        print "details=%s" %rex.details


    # Create a list of Ip addresses
    ipCfgList = []
    ipCfgList.append(Ip_cfg("1.1.1.1", "255.255.0.0"))
    ipAddress = Ethernet_ip_address(ipCfgList)

    # Ip has several subfields of which ip address is one of them
    ip = Ethernet_ip(ipAddress)
    ip.helper_address = '4.4.4.4'
    ip.cache_spoofing_port = 1
    ip.nat = Ethernet_ip_nat(outside=1)

    lacp_trunk_cfg = Ethernet_lacp_trunk_cfg (trunk=1, unidirectional_detection=1, mode='active')
    lacp = Ethernet_lacp(trunk_cfg=lacp_trunk_cfg, port_priority= 1)
    ethernet = Ethernet(ifnum=7, enable=1, ip=ip, load_interval= 5, mtu=1300, duplexity='Half')
    ddos = Ethernet_ddos(outside=1)

    ethernet.flow_control = 1
    ethernet.speed = 1000
    ethernet.lacp = lacp
    ethernet.ddos = ddos

    try :
        allEthernetsClient.submitInterfaceEthernet(ethernet)
    except interface_ethernet.RemoteException as rex:
        print (rex.status, rex.message, rex.details)



    # Get a List of all Ethernet objects
    try:
        allEthernets = allEthernetsClient.getAllInterfaceEthernets()
    except interface_ethernet.RemoteException as rex:
        print "status=%s" %rex.status
        print "message=%s" %rex.message
        print "details=%s" %rex.details


    # Get an ethernet object with a given interface index 7

    try:
        ethernetObject = ethernetIdClient.getInterfaceEthernet(Ethernet_ifnum(7))
    except interface_ethernet.RemoteException as rex:
        print (rex.status, rex.message, rex.details)

    print("interface=",ethernetObject.ifnum)
    print("mtu=",ethernetObject.mtu)
    if ethernet.ip:
        for ip_cfg in ethernetObject.ip.address.ip_cfg:
            print("ipv4-address=",ip_cfg.ipv4_address)
            print("ipv4-netmask=",ip_cfg.ipv4_netmask)


    # Restoring an interface ethernet 7 to default. Remove the comments below to test delete

    #try :
    #    ethernetIdClient.deleteEthernet(7)
    #except interface_ethernet.RemoteException as rex:
    #    print (rex.status, rex.message, rex.details)




