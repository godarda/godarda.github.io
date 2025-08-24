# ----------------------------------------------------------------------------------------------------
# Title          : Python program to check whether a given character is an alphabet
# File Name      : gdwmaxe.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

print("______________________________________________")
print("Program to check a character is alphabet")
print("______________________________________________")
c=input("Enter the character ")
if(len(c)==1):
    if(c=='a' or c=='A' or c=='e' or c=='E' or c=='i' or c=='I' or c=='o' or c=='O' or c=='u' or c=='U'):
        print(c,"is vowel and alphabet")
    elif((c>='a' and c<='z') or (c>='A' and c<='Z')):
        print(c,"is only an alphabet")
    else:
        print(c,"is not an alphabet")
elif(len(c)==0):
    print("Enter valid character")
else:
    print(c, "is set of characters")
print("______________________________________________")
