# ----------------------------------------------------------------------------------------------------
# Title          : Python progarm for Insertion Sort
# File Name      : gdaekky.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

def insertion_sort(nlist):
    for i in range(1, len(nlist)):
        key = nlist[i]
        j = i - 1

        while j >= 0 and key < nlist[j]:
            nlist[j + 1] = nlist[j]
            j = j - 1

        nlist[j + 1] = key
        print(nlist)

nlist = [12, 1024, -2048, 0, -1, 95, 987]
insertion_sort(nlist)
print(nlist)
