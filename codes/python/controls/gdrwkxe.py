# ----------------------------------------------------------------------------------------------------
# Title          : Python program to check whether a given year is a leap
# File Name      : gdrwkxe.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

print("__________________________________________")
print("Program to check the given year is leap or not")
print("__________________________________________")
try:
    y=input("Enter the year ")
    if(len(y)!=4 or int(y)<=0):
        print("Enter a valid year")
    else:
        year=int(y)
        if(year%4==0):
            if(year%100==0):
                if(year%400==0):
                    print("{0} is a leap year".format(year))
                else:
                    print("{0} is not a leap year".format(year))
            else:
                print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
except ValueError:
    print("Enter valid year")
print("__________________________________________")
