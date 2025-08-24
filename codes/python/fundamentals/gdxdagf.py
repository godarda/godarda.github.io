# ----------------------------------------------------------------------------------------------------
# Title          : Python program to print the current date and time
# File Name      : gdxdagf.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

import datetime
print("________________________________________")
print("Program to print the current date and time")
print("________________________________________")
now=datetime.datetime.now()
print("Date And Time | %s"%now)
print("ISO Format    | %s"%now.isoformat())
print("Year          | %s"%now.year)
print("Month         | %s"%now.month)
print("Day           | %s"%now.day)
print("DD/MM/YYYY    | %s/%s/%s"%(now.day,now.month,now.year))
print("Hour          | %s"%now.hour)
print("Minute        | %s"%now.minute)
print("Second        | %s"%now.second)
print("Microsecond   | %s"%now.microsecond)
print("HH:MM:SS      | %s:%s:%s"%(now.hour,now.minute,now.second))
print("________________________________________")
