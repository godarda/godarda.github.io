# ----------------------------------------------------------------------------------------------------
# Title          : Python progarm for Merge Sort
# File Name      : gdorpaw.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

def merge_sort(nlist):
    if len(nlist) > 1:
        mid = len(nlist) // 2
        lefthalf = nlist[:mid]
        print(" Left Split:", lefthalf)
        righthalf = nlist[mid:]
        print("Right Split:", righthalf)

        merge_sort(lefthalf)
        merge_sort(righthalf)
        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k] = lefthalf[i]
                i += 1
            else:
                nlist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            nlist[k] = lefthalf[i]
            i += 1
            k += 1
            print(" Left Merge:", nlist)

        while j < len(righthalf):
            nlist[k] = righthalf[j]
            j += 1
            k += 1
            print("Right Merge:", nlist)

nlist = [12, 1024, -2048, 0, -1, 95, 987]
merge_sort(nlist)
print(nlist)
