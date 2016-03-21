#!/usr/bin/env python

#
# v1, December 19, 2013
# by Eric Chou
#
# Reference: AX_aXAPI_Ref_v2-20121010.pdf
# Usage:
# python macAddress.py -d <device> -p <port>
# python macAddress.py -d 192.168.148.163 -p 1
#

import httplib, json, urllib, urllib2, optparse
import socket, ssl
from xml.etree import ElementTree

# specify device and command
parser = optparse.OptionParser()
parser.add_option('-d', '--device', dest="device", action="store")
parser.add_option('-p', '--port', dest="port", action="store")

options, args = parser.parse_args()
device = options.device
port = options.port

# patch httplib.HTTPSConnection.connect
def connect_patched(self):
    "Connect to a host on a given (SSL) port."

    sock = socket.create_connection((self.host, self.port),self.timeout, self.source_address)
    if self._tunnel_host:
        self.sock = sock
        self._tunnel()
    self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_TLSv1)

httplib.HTTPSConnection.connect = connect_patched


# Gets the session ID to
c = httplib.HTTPSConnection(device)
c.request("GET", "/services/rest/V2/?method=authenticate&username=admin&password=a10&format=json")
response = c.getresponse()
data = json.loads(response.read())
session_id = data['session_id']
print "Session Created. Session ID: " + session_id

# Construct HTTP URL and Post Body
post_body = ""
url = "https://" + device + "/services/rest/V2/?&session_id=" + session_id + "&format=json&method=network.interface.get&port_num="+port
print "URL Created. URL: " + url + " body: " + post_body

# Making request
req = urllib2.Request(url, post_body)
rsp = urllib2.urlopen(req)
content = rsp.read()

# parse XML tree
root = ElementTree.fromstring(content)
for i in root.iter('mac_addr'):
    print i.text
