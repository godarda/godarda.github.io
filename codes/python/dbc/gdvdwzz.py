# ----------------------------------------------------------------------------------------------------
# Title          : Python MySQL to connect, create a database, and table
# File Name      : gdvdwzz.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",passwd="godarda")
print("Connection Established")
cursor=db.cursor()

try:
    cursor.execute("CREATE DATABASE DB")
except:
    cursor.execute("DROP DATABASE DB")
    cursor.execute("CREATE DATABASE DB")
print("Database DB created successfully")

cursor.execute("SHOW DATABASES")
for dbs in cursor:
    print(dbs)
    
db.close()
