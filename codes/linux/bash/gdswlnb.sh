# ----------------------------------------------------------------------------------------------------
# Title          : Bash shell script to check a given number is positive or negative
# File Name      : gdswlnb.sh
# Compiled       : GNU bash, version 5.2.37(1)-release (x86_64-pc-linux-gnu)
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

#!/bin/bash

echo "———————————————————————————————————————————"
echo "Script to check a given number is +ve or -ve "
echo "———————————————————————————————————————————"
echo "Enter the number \c"; read a
b=0
if [ $a -gt $b ];then
    echo "Entered number is positive"
elif [ $a -eq $b ];then
    echo "Entered number is zero"
else
    echo "Entered number is negative"
fi
echo "———————————————————————————————————————————"
