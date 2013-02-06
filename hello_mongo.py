import pymongo

from pymongo import Connection

connection = Connection('localhost', 27017)#COMMAND: mongo --port 27017

db= connection.test

names = db.names # use names
                #db.insert({name:"a name"})

item = names.find_one()

print item['name']
