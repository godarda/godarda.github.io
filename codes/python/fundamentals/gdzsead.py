# ----------------------------------------------------------------------------------------------------
# Title          : Python program to demonstrate debugging of script
# File Name      : gdzsead.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

import pdb

def add(a):
    return a * a
pdb.set_trace()
a = input("A = ")
b = input("B = ")
c = int(a) + int(b)
print(c)
d = add(3)
print(d)
