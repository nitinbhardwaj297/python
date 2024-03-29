import pymongo
from pymongo import MongoClient
client = MongoClient()
client

print(client.list_database_names())