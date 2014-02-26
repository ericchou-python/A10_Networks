
################################################################################
# File name: test_ddos_dst_default.py
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

from sdk_auth import *
from ddos_dst_default import *

if __name__ == '__main__':

    host_ip = '10.3.150.184'
    enable_debug = False

    description = '\n\
    Description: \n\
    ------------ \n\
    1. Retrieve the signature after authorization. \n\
    2. Remove any configuration if it already exists for ddos dst default\n\
    3. Create TCP L4-type and UDP L4-Type, and create a Default object\n\
    4. Submit the object\n\
    5. Get a ddos dst default object of address type == ip and print the details'
    print(description)


    print("\n***** Retrieve signature *****")
    try :
        auth_client = AuthorizationClient(ipaddress=host_ip,debug=enable_debug)
        credentials = Credentials(username="admin", password="a10")
        auth_response = auth_client.submitCredentials(credentials)
        signature = auth_response.signature
    except RemoteException as re:
        print "status=%s" %re.status
        print "message=%s" %re.message
        print "details=%s" %re.details


    ########## Creating a new ddos dst default entry

    # For convenience we have two types of Https clients

    # All Ddos dst defaults Client
    all_ddos_dst_default_client = AllDdosDstDefaultsClient(ipaddress = host_ip, sessionid=signature, debug=enable_debug)
    # Ddos dst default Client
    ddos_dst_default_client = DdosDstDefaultClient(ipaddress = host_ip, sessionid=signature, debug=enable_debug)


    print("\n***** Remove any configuration if it already exists for ddos dst default *****")
    print("_____ Object specified does not exist error will show up if no ddos dst default configuration exists _____")


    try :
        ddos_dst_default_client.deleteDdosDstDefault(Default_default_address_type('ip'))
    except RemoteException as rex:
        print "status=%s" %rex.status
        print "message=%s" %rex.message
        print "details=%s" %rex.details


    print("\n***** Create TCP L4-type and UDP L4-Type, and create a Default object *****")
    l4_type_tcp = Ddos_dst_default_l4_type(protocol = 'tcp',
                                       deny = 1,
                                       syn_cookie = 1,
                                       tcp_reset_client = 1)
    l4_type_udp = Ddos_dst_default_l4_type(protocol = 'udp',
                                           stateful = 1,
                                           over_conn_limit_action = 'drop')
    default_object = Default(default_address_type = 'ip',
                age = 10,
                l4_typelist = [l4_type_tcp, l4_type_udp])

    print("\n***** Submit the object *****")
    try :
        all_ddos_dst_default_client.submitDdosDstDefault(default_object)
    except RemoteException as re:
        print "status=%s" %re.status
        print "message=%s" %re.message
        print "details=%s" %re.details



    print ("\n***** Get a ddos dst default object of address type == ip *****")

    try:
        ddos_dst_default_object = ddos_dst_default_client.getDdosDstDefault(Default_default_address_type('ip'))
        print ("Default address type:" + ddos_dst_default_object.default_address_type)
        print ("Age:" + str(ddos_dst_default_object.age))
        if (ddos_dst_default_object.l4_typelist):
            for l4_type in ddos_dst_default_object.l4_typelist:
                print ("Protocol:" + l4_type.protocol)
                if (l4_type.protocol == 'tcp'):
                    print ("Syn-cookie:" + str(l4_type.syn_cookie))
                if (l4_type.protocol == 'udp'):
                    print ("Stateful:" + str(l4_type.stateful))
    except RemoteException as re:
        print "status=%s" %re.status
        print "message=%s" %re.message
        print "details=%s" %re.details


    print("\n***** Logoff *****")
    auth_client.submitlogoff(credentials)

