# ----------------------------------------------------------------------------------------------------
# Title          : Python program to print the multiplication table of a given number
# File Name      : gdalmxy.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

print("________________________________________")
print("Program to print the multiplication table")
print("________________________________________")
try:
    n=int(input("Enter the number "))
    if(n<=0):
        print("Please enter a positive number")
    else:
        for i in range(1,11):
            print(n,"*",i,"=",n*i)
except ValueError:
    print("Enter valid number")
print("________________________________________")
