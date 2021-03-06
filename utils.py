# Some helper functions.
# You should not need to edit this file.

import ujson
import fileinput

from pymongo import connection

from settings import torn_settings 

def read_beers():
    for line in fileinput.input():
        yield ujson.loads(line)

def connect_db(dbname, remove_existing=False):
    con = connection.Connection(torn_settings['mongo_host'],torn_settings['mongo_port'])
    if remove_existing:
        con.drop_database(dbname)
    return con[dbname]



