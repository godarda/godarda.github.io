# ----------------------------------------------------------------------------------------------------
# Title          : Python program to check whether a given number is a palindrome
# File Name      : gdggkza.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

print("____________________________________________")
print("Program to check number is palindrome or not")
print("____________________________________________")
n=int(input("Enter the number "))
temp=n
r=0
while(n>0):
    r=(r*10)+n%10
    n=n//10
print("Reverse number is",r)
if(temp==r):
    print(temp, "is palindrome")
else:
    print(temp, "is not palindrome")
print("____________________________________________")
