# ----------------------------------------------------------------------------------------------------
# Title          : Python MongoDB to connect, create database, and collection
# File Name      : gdmyyzz.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

import pymongo
from pymongo import MongoClient
client=MongoClient()
print("Connection Established")

# client=MongoClient('localhost',27017)
# db=client.DB
# collection=db.holders

client=MongoClient('mongodb://localhost:27017/')
db=client['DB']
collection=db['holders']

holder1={
'account_no': 2562348989,
'name': 'James Moore',
'bank': 'Barclays',
'amount': 5000
}

doc=db.holders.insert_one(holder1)
print("\nCollection Name(s): ",db.list_collection_names())
# print(db.holders.find_one())
print("\nFirst document key: {}".format(doc.inserted_id))
