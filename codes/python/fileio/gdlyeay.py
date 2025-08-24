# ----------------------------------------------------------------------------------------------------
# Title          : Python program to count the frequency of words in a given file
# File Name      : gdlyeay.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

from collections import Counter
char=0
lines=0
for line in open(r'/home/godarda/Weekdays'):
    char=char+len(line)
    lines+=1
print("Characters -",char)
print("Lines -",lines)

with open(r'/home/godarda/Weekdays') as f:
    words=[word for line in f for word in line.split()]
    print("Word Count -",len(words))
    c=Counter(words)
    for word,count in c.most_common():
        print(word,"-",count)
