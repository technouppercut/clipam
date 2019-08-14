#!/bin/python3

import sys
import os
import subprocess
import clihelp
import newdev
from optparse import OptionParser
########################################


[...]

def main():

    parser = OptionParser()

    parser.add_option("-i", "--ipaddr", help="Device IP Address")
    parser.add_option("-n", "--netmask", help="Device Netmask")
    parser.add_option("-d", "--device", help="Device Hostname")
    parser.add_option("-c", "--comment", help="Device Comment Or Description")

    [...]

    (options, args) = parser.parse_args()

    if len(args) == 0:
        clihelp.menu_help()

    else:
        os.system('python3 clipdb.py' + ' ' + option.ipaddr + ' ' + option.netmask + ' ' + option.device + ' ' + option.comment)
        #newdev.addip(option.ipaddr + ' ' + option.netmask + ' ' + option.device + ' ' + option.comment)
    [...]

if __name__ == "__main__":
    main()
