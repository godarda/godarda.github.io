# ----------------------------------------------------------------------------------------------------
# Title          : Python implementation of Binary Search
# File Name      : gdwzavz.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

def BinarySearch(array,num,first,last):
    if(first>last):
        print("\nElement not found!")
        print("———————————————————————————————————————————")
    else:
        mid=(first+last)//2;
        if(array[mid]==num):
            print("\nElement found at index",mid+1)
            print("———————————————————————————————————————————")
        elif(array[mid]>num):
            BinarySearch(array,num,first,mid-1);
        else:
            BinarySearch(array,num,mid+1,last);

print("———————————————————————————————————————————")
print("Implementation of a Binary Search")
print("———————————————————————————————————————————")
try:
    array=[]
    n=int(input("How many numbers you want to enter "))
    if(n>0):
        for i in range(0,n):
            print("Enter Number",i+1,end=" | ")
            numbers=int(input())
            array.append(numbers)
        array.sort()
        print("\nSorted numbers",array)
        num=int(input("\nEnter the number to be searched "))
        beg=0
        end=n-1
        BinarySearch(array,num,beg,end)
    else:
        print("\nPlease enter a positive integer")
        print("———————————————————————————————————————————")
except ValueError:
    print("\nInvalid Input!\nProgram Terminated")
    print("———————————————————————————————————————————")
