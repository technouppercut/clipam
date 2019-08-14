#!/usr/bin/python3

import sys
import os
import datetime
from easySqlite3 import Db



#VARS############################
path = os.getcwd()
now = datetime.datetime.now()
#Open Logfile
logfile = open('applog.txt', 'a')
sys.stdout = logfile
#################################
print("Clipam Logfile")
print(now)

#Create Directory
try:
    os.mkdir(path + '/data')
except OSError:
    print ("Directory Creation Has Failed For Directory: /data ")
else:
    print ("Directory Creation Was Successful For Directory: /data ")




#Create Database
print("Building Database: ipdb.sql @: /data/ ")

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

db = Db(DATA_BASE_PATH)

db.connect()

#Close Database
db.close()

#Close Logfile
logfile.close()






