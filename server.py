#!/usr/bin/python
import socket
import sys
import time
import ConfigParser
import os

#Write PID
pid = str(os.getpid())
f = open('/tmp/pysocket.pid', 'w')
f.write(pid)
f.close()

config = ConfigParser.RawConfigParser()
config.readfp(open('/tmp/defaults.cfg'))
PORTS = [e.strip() for e in config.get('settings', 'PORTS').split(',')]

HOST = ''   # Symbolic name, meaning all available interfaces

s={}
sockets = 0

for p in PORTS:
 s[sockets] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s[sockets].bind((HOST,int(p)))
 s[sockets].listen(10)
 print "Listening on: ", p
 sockets += 1

print "Waiting for connections"

while 1:
    time.sleep(60)
s.close()

