# ----------------------------------------------------------------------------------------------------
# Title          : Python program to count the lines, words, and characters from a given file
# File Name      : gddzeng.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

import string
data = open('/home/godarda/Weekdays', 'r').read()
print("Characters - %s"%(len(data)))
print("Lines - %s"%(len(data.splitlines())))
print("Words - %s"%(len(str.split(data))))
