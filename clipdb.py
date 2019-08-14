#!/usr/bin/python3

import sys
import os
import datetime
from easySqlite3 import Db

#VARS############################
now = datetime.datetime.now()
#Open Logfile
logfile = open('applog.txt', 'a')
sys.stdout = logfile
#################################
print("Clipam Logfile")
print(now)





TABLE = '''
        CREATE TABLE IF NOT EXISTS netdevs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        IPAddress TEXT NOT NULL,
        Netmask TEXT NOT NULL,
        Device TEXT NOT NULL,
        Comments TEXT NULL
        );
        '''

DATA_BASE_PATH = 'data/ipdb.sql'
#db = 'data/ipdb.sql'
INSERT_QUERY = 'INSERT INTO netdevs(IPAddress, Netmask, Device, Comments) VALUES (?, ?, ?, ?)'


# start an data base object
db = Db(DATA_BASE_PATH)

# connect to the data base
db.connect()

# create the table
db.createTable(TABLE)

# prepare query
db.prepareQuery(INSERT_QUERY)

#        print('Clipam Help Menu')
#        print("clipam <ip addr> <netmask> <hostname> <comment>")
#        print("clipam 1.1.1.1 255.255.255.0 giga.ios.devicename CoreRouter")

netdev_ip = sys.argv[1]
netdev_netmask = sys.argv[2]
netdev_device = sys.argv[3]
netdev_comment = sys.argv[4]

print("Device Entry: ")
print("   IP      NETMASK      DEVICE  ")
print(netdev_ip + ' ' + netdev_netmask + ' ' + netdev_device)


# insert into table
db.insertRow([netdev_ip, netdev_netmask, netdev_device, netdev_comment])

# closing connection
db.close()



logfile.close()
