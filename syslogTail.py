#!/usr/env/bin python
#
# Eric Chou ericc@a10networks.com
# Fred Hsu fredlhsu@aristanetworks.com
#
# Feb. 15, 2014

import RPi.GPIO as GPIO
import subprocess, time, re
from jsonrpclib import Server

p = subprocess.Popen('tail -f /var/log/syslog', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

#set up GPIO pin 18
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT) #LED out
GPIO.setup(17, GPIO.IN) #Motion detection
GPIO.setup(18, False)

# Motion sensor kicks off the sequence of events
while True:
    input_state = GPIO.input(17)
    print ("Wave your hand in front of the sensor to activate")
    if input_state == True:
        print("Motion Detected")
        break

# Sets Arista API call parameters
username = "admin"
password = "admin"
switch = "172.22.28.156"
dip = "10.1.1.1"
outport = "Port-Channel 100"
urlString = "https://{}:{}@{}/command-api".format(username, password, switch)
switchReq = Server( urlString )

# Tails syslog and look for the re expression
while True:
    line = (p.stdout.readline()).strip()
    if re.search('vThunder-2', line):
        print "Found Event: ", line
        GPIO.output(18, True)
        print "Pushing Direct Flow out to Arista switch", switch
        # The following rpc request will match on the source IP, then punts traffic to output port
        response = switchReq.runCmds( 1, ["enable", "configure", "openflow", "flow a10", "persistent", "match destination ip {}".format(dip), "action set output interface {}".format(outport)] )

