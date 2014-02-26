
################################################################################
# File name: test_ddos_src_entry.py
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
from ddos_src_entry import *
from ddos_template_tcp import *
from ddos_template_udp import *

if __name__ == '__main__':

    host_ip = '10.3.150.184'
    enable_debug = False

    description = '\n\
    Description: \n\
    ------------ \n\
    1. Retrieve the signature after authorization. \n\
    2. Create new ddos templates for TCP and UDP. \n\
    3. Remove any pre-existing configuration for ddos src entry\n\
    4. Create a list of l4-types and use it in a ddos src entry object\n\
    5. Submit the object\n\
    6. Print details about the ddos src entry.'
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



    print("\n***** Creating new ddos templates for tcp and udp *****")
    all_ddos_template_tcp_client = AllDdosTemplateTcpsClient(ipaddress = host_ip, sessionid=signature, debug=enable_debug)
    all_ddos_template_udp_client = AllDdosTemplateUdpsClient(ipaddress = host_ip, sessionid=signature, debug=enable_debug)

    try:
        all_ddos_template_tcp_client.submitDdosTemplateTcp(Tcp(name='TCP_TEMPLATE', age=10))
        all_ddos_template_udp_client.submitDdosTemplateUdp(Udp(name='UDP_TEMPLATE', age=20))
    except RemoteException as rex:
        print "status=%s" %rex.status
        print "message=%s" %rex.message
        print "details=%s" %rex.details


    # For convenience we have two types of Https clients
    # All Ddos src entry Client
    all_ddos_src_entry_client = AllDdosSrcEntrysClient(ipaddress = host_ip, sessionid=signature, debug=enable_debug)
    # Ddos src entry Client
    ddos_src_entry_client = DdosSrcEntryClient(ipaddress = host_ip, sessionid=signature, debug=enable_debug)


    print("\n***** Remove any configuration if it already exists for ddos src entry *****")
    print("_____ Object specified does not exist error will show up if no ddos src entry configuration exists _____")
    try :
        ddos_src_entry_client.deleteDdosSrcEntry(Entry_src_entry_name('US-gateway'))
    except RemoteException as rex:
        print "status=%s" %rex.status
        print "message=%s" %rex.message
        print "details=%s" %rex.details


    print("\n***** Create a list of l4types *****")

    l4_type_tcp_template = Ddos_src_entry_l4_type__template('TCP_TEMPLATE')
    l4_type_tcp = Ddos_src_entry_l4_type(protocol = 'tcp', template = l4_type_tcp_template)

    src_entry_object = Entry(src_entry_name= 'US-gateway',ip_addr = '2.2.2.2',
                l4_typelist = [l4_type_tcp])

    print("\n***** Submit the Ddos src entry *****")
    try :
        all_ddos_src_entry_client.submitDdosSrcEntry(src_entry_object)
    except RemoteException as rex:
        print ("Rex" , rex.status, rex.message, rex.details)



    print ("\n***** Retrieve a ddos src entry object of name = US-gateway *****")

    try:
        ddos_src_entry_object = ddos_src_entry_client.getDdosSrcEntry(Entry_src_entry_name('US-gateway'))
        print("Entry name:" + ddos_src_entry_object.src_entry_name)
        print("IPv4 Address:" + str(ddos_src_entry_object.ip_addr))
        if (ddos_src_entry_object.l4_typelist):
            for l4_type in ddos_src_entry_object.l4_typelist:
                print("Protocol:" + l4_type.protocol)
                template = l4_type.template
                if template:
                    print("Template Name:" + str(template.tcp))
    except RemoteException as rex:
        print (rex.status, rex.message, rex.details)


    print("\n***** Logoff *****")
    auth_client.submitlogoff(credentials)
