# ----------------------------------------------------------------------------------------------------
# Title          : Python program to print the list of all leap years
# File Name      : gdrawfa.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

print("________________________________________")
print("Program to print the list of all leap years")
print("________________________________________")
y=int(input("How many years you want to print "))
if(y<1):
    print("Enter the valid number of years")
else:
    lc=0
    for i in range(y):
        year=2024+i
        if(year%4==0):
            if(year%100==0):
                if(year%400==0):
                    print("{0} is a leap year".format(year))
                    lc=lc+1
                else:
                    print("{0} is not a leap year".format(year))
            else:
                print("{0} is a leap year".format(year))
                lc=lc+1
        else:
            print("{0} is not a leap year".format(year))
    print("Total leap years between 2024 to {0} is".format(year),lc)
print("________________________________________")
