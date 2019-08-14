#!/usr/bin/python3

from easySqlite3 import Db

TABLE = '''
        CREATE TABLE IF NOT EXISTS netdevs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        IPAddress TEXT NOT NULL,
        Netmask TEXT NOT NULL,
        Device TEXT NOT NULL,
        Comments TEXT NULL
        );
        '''

DATA_BASE_PATH = 'ipdb.sql'
INSERT_QUERY = 'INSERT INTO netdevs(IPAddress, Netmask, Device, Comments) VALUES (?, ?, ?, ?)'


# start an data base object
db = Db(DATA_BASE_PATH)

# connect to the data base
db.connect()

# create the table
db.createTable(TABLE)

# prepare query
db.prepareQuery(INSERT_QUERY)


netdev_ip = input('Input IPAddress: ')
netdev_netmask = input('Input Netmask: ')
netdev_device = input('Input Device: ')
netdev_comment = input('Input Comments: ')


# insert into table
db.insertRow([netdev_ip, netdev_netmask, netdev_device, netdev_comment])

# closing connection
db.close()
