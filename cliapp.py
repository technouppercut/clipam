#!/bin/python3

import sys
import os
import subprocess
import clihelp
from optparse import OptionParser
########################################


[...]
parser = OptionParser()

parser.add_option("-i", "--ipaddr", help="Device IP Address")
parser.add_option("-n", "--netmask", help="Device Netmask")
parser.add_option("-d", "--device", help="Device Hostname")
parser.add_option("-c", "--comment", help="Device Comment Or Description")

(options, args) = parser.parse_args()

#print(options.ipaddr)
#print(options.netmask)
#subprocess.call(["python3 clipdb.py"])
if len(args) == 0:
    clihelp.menu_help()
else:
    os.system('python3 clipdb.py' + ' ' + options.ipaddr + ' ' + options.netmask + ' ' + options.device + ' ' + options.comment)
