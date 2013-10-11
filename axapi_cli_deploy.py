#!/usr/bin/env python

#
# v1, September 30, 2013
# by Eric Chou
#
# Reference: AX_aXAPI_Ref_v2-20121010.pdf
#

import httplib, json, urllib, urllib2, optparse

# specify device and command
parser = optparse.OptionParser()
parser.add_option('-d', '--device', dest="device", action="store")
parser.add_option('-c', '--command', dest="commandFile", action="store")


options, args = parser.parse_args()
device = options.device
commandFile = options.commandFile


# Gets the session ID
c = httplib.HTTPSConnection(device)
c.request("GET", "/services/rest/V2/?method=authenticate&username=admin&password=a10&format=json")
response = c.getresponse()
data = json.loads(response.read())
session_id = data['session_id']
print "Session Created. Session ID: " + session_id

# Construct HTTP URL and Post Body
post_body = open(commandFile, 'r').read()
url = "https://" + device + "/services/rest/V2/?&session_id=" + session_id + \
      "&format=json&method=cli.deploy&username=admin&password&a10&enable_password=''&grab_config=1"
print "URL Created. URL: " + url + " body: " + post_body 

# Making request 
req = urllib2.Request(url, post_body)
rsp = urllib2.urlopen(req)
content = rsp.read()
print "Result: " + content

