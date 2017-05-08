#Mighty Python is a part of BoKode.inc and is not responsible for the damage done by users with destuctive purposes (if any) when using this library.


#Organization: BoKode
#Owner: ninjabobroberts
#Team: Group A

#This library is a

import getopt
import os
import sys
import subprocess


platform1 = ''

def getplatform():
    if sys.platform.startswith('linux'):
        platform1 = 'linux'
        print "Using Linux Version"
    elif sys.platform.startswith('win32'):
        platform1 = 'windows'
        print "Using Windows Version"
    elif sys.platform.startswith('darwin'):
        platform1 = 'mac'
        print "Using Mac OS Version"
    elif sys.platform.startswith('cygwin'):
        platform1 = 'windows'
    else:
        print "Unrecagnized Platform"

def get_modules(modules):
    module = raw_input("What Modules Do You Want To Update?")
    download = raw_input("Do You Have Pip? y/n")
    if download == "y":
        if platform1 == 'linux' or 'mac':
            try:
                Cmd1 = os.system("pip install ", module, "--upgrade")
                Output1 = subprocess.check_output(Cmd1, shell=True)
                print Output1
            except:
                print "Something went wrong. Do you have pip installed?\nTo check type in terminal 'pip install [module]
        elif platform1 == 'windows':
            Cmd2 = os.system("pip install ", module, "--upgrade")
            Output2 = subprocess.check_output(Cmd2, shell=True)
            print Output2
        else:
            print "Unrecagnized Platform"
            print "Look At The Source Code For Help And Debugging"
    else:
        if platform1 == 'linux' or 'mac':
            try:
                Cmd3 = os.system("sudo apt-get install python-setuptools python-dev build-essential")
                Output3 = subprocess.check_output(Cmd3, shell=True)
                Cmd4 = os.system("sudo easy_install pip")
                Output4 = subprocess.check_output(Cmd4, shell=True)
                print "First try: ", Output2, "Second try: " Output3
                Cmd5 = os.system("pip install ", module, "--upgrade")
                Output5 = subprocess.check_output(Cmd5, shell=True)
            except:
                print "Something went wrong"


def list_outdated_modules():
    if platfrom == 'linux' or 'mac':
        
            
            
                        


    
#os.putenv(mightypython, mightypython)
#os.unsetenv(mightypython, mightypython)
#sys.platform(


def copyrights():
    print "This is the Mighty Python Module used for updating outdated modules.\nThis can be useful for online projects, web apps etc.\nThe module is part of BoKode and will stay that way."

#def main(module_num):
