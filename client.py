#!/usr/bin/python

import socket
import sys
import ConfigParser

config = ConfigParser.RawConfigParser()
config.readfp(open('/tmp/defaults.cfg'))
HOSTS = [e.strip() for e in config.get('settings', 'HOSTS').split(',')]
PORTS = [e.strip() for e in config.get('settings', 'PORTS').split(',')]

def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      print "\x1b[6;30;42m  \x1b[0m" + ip + ":" + port, 'is up'
      return True
   except:
      print "\x1b[0;30;41m  \x1b[0m" + ip + ":" + port, 'is down'
      return False

print "\033[1mTesting from: ", socket.gethostname() , "\x1b[0m"
for h in HOSTS:
	for p in PORTS:
		isOpen(h,p)
