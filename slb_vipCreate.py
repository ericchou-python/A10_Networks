#!/usr/bin/env python

#
# v1, September 27, 2013
# by Eric Chou
#
# Reference: AX_aXAPI_Ref_v2-20121010.pdf
#

import httplib, json, urllib, urllib2

# Gets the session ID to host 172.31.31.121 (Student 12)
c = httplib.HTTPSConnection("172.31.31.121")
c.request("GET", "/services/rest/V2/?method=authenticate&username=admin&password=a10&format=json")
response = c.getresponse()
data = json.loads(response.read())
session_id = data['session_id']
print "Session Created. Session ID: " + session_id

###############################
#  Step 1. Create Servers     #
###############################

# Create slb servers s1 10.0.2.128 
# Construct HTTP URL and Post Body
post_body = json.dumps(
	{"server":
         {
          "name": "s1",
          "host": "10.0.2.128",
          "health_monitor": "(default)",
          "port_list": [
           {"port_num": 80,
            "protocol": 2,}
          ],
          }     
	}
)
url = "https://172.31.31.121/services/rest/V2/?&session_id=" + session_id + "&format=json&method=slb.server.create"
print "URL Created. URL: " + url + " body: " + post_body 

# Making request 
req = urllib2.Request(url, post_body)
rsp = urllib2.urlopen(req)
content = rsp.read()
print "Result: " + content

# Create slb server s2 10.0.2.129
post_body = json.dumps(
	{"server":
         {
          "name": "s2",
          "host": "10.0.2.129",
          "health_monitor": "(default)",
          "port_list": [
           {"port_num": 80,
            "protocol": 2,}
          ],
          }     
	}
)
url = "https://172.31.31.121/services/rest/V2/?&session_id=" + session_id + "&format=json&method=slb.server.create"
print "URL Created. URL: " + url + " body: " + post_body 

# Making request 
req = urllib2.Request(url, post_body)
rsp = urllib2.urlopen(req)
content = rsp.read()
print "Result: " + content

####################################
#  Step 2. Create Service Group    #
####################################

# Create service group http with member server s1 and s2
post_body = json.dumps(
	{"service_group":
         {
          "name": "http",
          "protocol": 2,
          "health_monitor": "ping",
          "member_list": [
           {"server": "s1",
            "port": 80,},
           {"server": "s2",
            "port": 80,},
          ],
          }     
	}
)
url = "https://172.31.31.121/services/rest/V2/?&session_id=" + session_id + "&format=json&method=slb.service_group.create"
print "URL Created. URL: " + url + " body: " + post_body 

# Making request 
req = urllib2.Request(url, post_body)
rsp = urllib2.urlopen(req)
content = rsp.read()
print "Result: " + content

#####################################
#  Step 3. Create Virtual Server    #
#####################################

# Create virtual server
post_body = json.dumps(
	{"virtual_server":
         {
          "name": "vip1",
          "subnet":
           {
            "address": "10.0.1.122",
            "mask_len": 24,
           },
          "vport_list": [
           {"protocol": 2,
            "port": 80,
            "service_group": "http",
            },
          ],
          }  
	}
)
url = "https://172.31.31.121/services/rest/V2/?&session_id=" + session_id + "&format=json&method=slb.virtual_server.create"
print "URL Created. URL: " + url + " body: " + post_body 

# Making request 
req = urllib2.Request(url, post_body)
rsp = urllib2.urlopen(req)
content = rsp.read()
print "Result: " + content

