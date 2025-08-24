# ----------------------------------------------------------------------------------------------------
# Title          : Python progarm for Bubble Sort
# File Name      : gdyezyi.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

def bubble_sort(nlist):
    for length in range(len(nlist)):
        for i in range(length):
            if nlist[i] > nlist[i + 1]:
                # nlist[i],nlist[i+1]=nlist[i+1],nlist[i]
                temp = nlist[i]
                nlist[i] = nlist[i + 1]
                nlist[i + 1] = temp
                print(nlist)

nlist = [12, 1024, -2048, 0, -1, 95, 987]
bubble_sort(nlist)
print(nlist)
