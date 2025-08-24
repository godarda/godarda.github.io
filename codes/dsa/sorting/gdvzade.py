# ----------------------------------------------------------------------------------------------------
# Title          : Python progarm for Quick Sort
# File Name      : gdvzade.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

def quick_sort(nlist):
    quicksort(nlist, 0, len(nlist) - 1)

def quicksort(nlist, first, last):
    if first < last:
        print(nlist)
        splitpoint = partition(nlist, first, last)
        quicksort(nlist, first, splitpoint - 1)
        quicksort(nlist, splitpoint + 1, last)

def partition(nlist, first, last):
    pivotvalue = nlist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and nlist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while nlist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
            if rightmark < leftmark:
                done = True
            else:
                temp = nlist[leftmark]
                nlist[leftmark] = nlist[rightmark]
                nlist[rightmark] = temp
        temp = nlist[first]
        nlist[first] = nlist[rightmark]
        nlist[rightmark] = temp
        return rightmark

nlist = [12, 1024, -2048, 0, -1, 95, 987]
quick_sort(nlist)
print(nlist)
