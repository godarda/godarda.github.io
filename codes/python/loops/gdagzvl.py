# ----------------------------------------------------------------------------------------------------
# Title          : Python program to find the factorial of a given number
# File Name      : gdagzvl.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

print("________________________________________")
print("Program to find the factorial of number")
print("________________________________________")
n=int(input("Enter the number "))
if(n<0):
    print("Factorial does not exits for",n)
else:
    fact=1
    while(n>0):
        fact=fact*n
        n=n-1
    print("Factorial",fact)
print("________________________________________")
