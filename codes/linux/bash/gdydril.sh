# ----------------------------------------------------------------------------------------------------
# Title          : Bash shell script to convert Decimal to Hexadecimal and Octal
# File Name      : gdydril.sh
# Compiled       : GNU bash, version 5.2.37(1)-release (x86_64-pc-linux-gnu)
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

#!/bin/bash

echo "———————————————————————————————————————————"
echo "Script to convert Dec To Hex and Oct number"
echo "———————————————————————————————————————————"
a=65535
echo -n "Decimal="$a
printf "\nOctal="%o $a
printf "\nHexadecimal="%x $a
echo -e "\n———————————————————————————————————————————"
