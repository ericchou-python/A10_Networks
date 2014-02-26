
################################################################################
# File name: show_ddos.py
# Copyright(C) 2007-2013, A10 Networks Inc. All rights reserved.
# Software for all A10 products contain trade secrets and confidential
# information of A10 Networks and its subsidiaries and may not be
# disclosed, copied, reproduced or distributed to anyone outside of
# A10 Networks without prior written consent of A10 Networks, Inc.
################################################################################
import sys
sys.path.append(".")
#sys.path.append("../..")
sys.path.append("/home/echou/a10API/app/scripts/axapisdk")
import python_sdk
from ddos_dst import *
from ddos_src import *
from sdk_auth import *


host_ip = '10.3.150.184'
enable_debug = False




description = '\n\
Description: \n\
------------ \n\
1. Retrieve the signature after authorization. \n\
2. Print the IPv4 address or Subnet address of ddos dst entries. \n\
3. Print the IPv4 address or Subnet address of ddos src entries.'
print(description)

print ("\n***** Retrieve signature *****")
try :
    auth_client = AuthorizationClient(ipaddress=host_ip,debug=enable_debug)
    credentials = Credentials(username="admin", password="a10")
    auth_response = auth_client.submitCredentials(credentials)
    signature = auth_response.signature
except RemoteException as re:
    print "status=%s" %re.status
    print "message=%s" %re.message
    print "details=%s" %re.details


print ("\n***** Print all ddos dst objects *****")
ddos_dst_client = DdosDstClient(ipaddress = host_ip, sessionid = signature, debug=enable_debug)
try:
    all_ddos_dst = ddos_dst_client.getDdosDst()
    if all_ddos_dst:
        entry_list = all_ddos_dst.entrylist
        if entry_list:
            for entry in entry_list:
                subnet = entry.subnet_ip_addr
                if subnet:
                    print("Dst Dst Entry Name:" + str (entry.dst_entry_name)+ " Subnet:" + str (entry.subnet_ip_addr))
                else:
                    print("Dst Dst Entry Name:" + str (entry.dst_entry_name)+ " IP:" + str (entry.ip_addr))
except RemoteException as re:
    print "status=%s" %re.status
    print "message=%s" %re.message
    print "details=%s" %re.details



print("\n***** Print all ddos src objects *****")
ddos_dst_client = DdosSrcClient(ipaddress = host_ip, sessionid = signature, debug=enable_debug)
try:
    all_ddos_src = ddos_dst_client.getDdosSrc()
    if all_ddos_src:
        entry_list = all_ddos_src.entrylist
        if entry_list:
            for entry in entry_list:
                subnet = entry.subnet_ip_addr
                if subnet:
                    print("Dst Src Entry Name:" + str (entry.src_entry_name)+ " Subnet:" + str (entry.subnet_ip_addr))
                else:
                    print("Dst Src Entry Name:" + str (entry.src_entry_name)+ " IP:" + str (entry.ip_addr))

except RemoteException as re:
    print "status=%s" %re.status
    print "message=%s" %re.message
    print "details=%s" %re.details


print("\n***** Logoff *****")
auth_client.submitlogoff(credentials)
