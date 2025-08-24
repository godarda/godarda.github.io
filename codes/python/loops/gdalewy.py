# ----------------------------------------------------------------------------------------------------
# Title          : Python program to print the sum of all digits in a given number
# File Name      : gdalewy.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

print("___________________________________________")
print("Program to print sum of all digits")
print("___________________________________________")
try:
    n=int(input("Enter the number "))
    if(n<=0):
        print("Please enter a positive number")
    else:
        sum=0
        temp=n
        while n>0:
            r=n%10
            sum=sum+r
            n=n//10
        print("Sum of all digits in",temp,"is",sum)
except ValueError:
    print("Enter valid number")
print("___________________________________________")
