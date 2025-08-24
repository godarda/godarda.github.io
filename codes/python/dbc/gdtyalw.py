# ----------------------------------------------------------------------------------------------------
# Title          : Python MySQL to insert and retrieve the records from a table
# File Name      : gdtyalw.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

import pymysql
import csv

tablename="holders"

try:
    db=pymysql.connect(host='localhost', user='root', password='godarda', database='DB')
    print("Connection Established")
    cursor=db.cursor()

    with open('gd.csv') as csvfile:
        reader=csv.reader(csvfile, delimiter=',')
        next(csvfile) #skip header row
        for row in reader:
            query="INSERT INTO {}(account_no, name, bank, amount) VALUES(%s, %s, %s, %s)".format(tablename)
            cursor.execute(query,row)
            db.commit()
    print("Records inserted successfully\n")
    
    print("Retrived records from a table")
    cursor.execute("SELECT * FROM {}".format(tablename))
    for records in cursor:
        print(records)
    
    print("\nRetrived records from a table")
    cursor.execute("SELECT * FROM {} WHERE amount >= 10000".format(tablename))
    for records in cursor:
        print(records)
    
    db.close()
except pymysql.Error as err:
    print("Error: {}".format(err))
