# ----------------------------------------------------------------------------------------------------
# Title          : Python MongoDB to insert and retrieve the documents from a collection
# File Name      : gdgulma.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

import pymongo
from pymongo import MongoClient
client=MongoClient()
print("Connection Established")

client=MongoClient('localhost',27017)
db=client.DB
collection=db.holders

holder1={
'account_no': 2562348989,
'name': 'James Moore',
'bank': 'Barclays',
'amount': 5000
}

holder2={
'account_no': 2562348990,
'name': 'Donald Taylor',
'bank': 'Citi',
'amount': 7000
}

holder3={
'account_no': 2562348991,
'name': 'Edward Parkar',
'bank': 'ICICI',
'amount': 95000
}

docs=db.holders.insert_many([holder1,holder2,holder3])
print("Documents inserted successfully")

for holder in db.holders.find():
    print(holder,"\n")

# Disabled _id attribute
for holder in db.holders.find({},{'_id': 0,'account_no': 1,'name':1}):
    print(holder)
