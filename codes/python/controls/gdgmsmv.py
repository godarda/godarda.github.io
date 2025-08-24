# ----------------------------------------------------------------------------------------------------
# Title          : Python program to check the equality of given numbers
# File Name      : gdgmsmv.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

print("__________________________________________")
print("Program for comparison of two numbers")
print("__________________________________________")
a=int(input("Enter the 1st number "))
b=int(input("Enter the 2nd number "))

if(a<b):
    print(a,"is less than",b)
elif(a==b):
    print(a,"is equal to",b)
else:
    print(a,"is greater than",b)
    
print("__________________________________________")
