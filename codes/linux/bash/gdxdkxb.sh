# ----------------------------------------------------------------------------------------------------
# Title          : Bash shell script to check the equality of a given numbers and strings
# File Name      : gdxdkxb.sh
# Compiled       : GNU bash, version 5.2.37(1)-release (x86_64-pc-linux-gnu)
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

#!/bin/bash

echo "———————————————————————————————————————————"
echo "Script to check the equality of given numbers"
echo "———————————————————————————————————————————"
echo -n "Enter the 1st number "; read a
echo -n "Enter the 2nd number "; read b
if [ $a -gt $b ];then
    echo "$a is greater than $b"
elif [ $a -eq $b ];then
    echo "$a is equal to $b"
else
    echo "$a is less than $b"
fi
echo "———————————————————————————————————————————"
