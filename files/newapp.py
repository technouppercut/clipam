#!/bin/python3

import sys
import os
import argparse
import newdev
import clihelp

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ipaddr", help="Device IP Address")
parser.add_argument("-n", "--netmask", help="Device Netmask")
parser.add_argument("-d", "--device", help="Device Hostname", required=True)
parser.add_argument("-c", "--comment", help="Device Comments Or Description")
parser.add_argument("-f", "--find", help="Find Device")
parser.add_argument("-r", "--remove", help="Remove Device")

options = parser.parse_args()

# then just pass in the arguments when you run the function
newdev.addip(ipaddress=options.ipaddr,
             netmask=options.netmask, 
             device=options.device,
             hostname=options.device,
             description=options.comment)





(options, args) = parser.parse_args()

if len(args) == 1:
    clihelp.menu_help()

else:
    os.system('python3 clipdb.py' + ' ' + options.ipaddr + ' ' + options.netmask + ' ' + options.device + ' ' + options.comment)

