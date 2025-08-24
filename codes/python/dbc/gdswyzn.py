# ----------------------------------------------------------------------------------------------------
# Title          : Python MySQL to update the table records
# File Name      : gdswyzn.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

import pymysql
import csv

tablename="holders"
update=(2000, 25622348993) #packing
(bonus, accno)=update #unpacking

try:
    db=pymysql.connect(host='localhost', user='root', password='godarda', database='DB')
    print("Connection Established")
    cursor=db.cursor()

    def RetrieveRecords():
        cursor.execute("SELECT * FROM {}".format(tablename))
        print("\nRetrived updated records from a table")
        for records in cursor:
            print(records)
    
    query="UPDATE {} SET amount = amount + %s WHERE account_no = %s".format(tablename)
    cursor.execute(query,update)
    db.commit()
    RetrieveRecords()
        
    query="UPDATE {} SET amount = amount + %s".format(tablename)
    cursor.execute(query,bonus)
    db.commit()
    RetrieveRecords()
    
    db.close()
except pymysql.Error as err:
    print("Error: {}".format(err))
