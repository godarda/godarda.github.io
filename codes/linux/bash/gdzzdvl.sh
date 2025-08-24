# ----------------------------------------------------------------------------------------------------
# Title          : Bash shell script to convert all uppercase letters in a file to lowercase letters
# File Name      : gdzzdvl.sh
# Compiled       : GNU bash, version 5.2.37(1)-release (x86_64-pc-linux-gnu)
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

#!/bin/bash

echo '___________________________________________'
echo 'Script to convert Uppercase to Lowercase'
echo '___________________________________________'
echo "1.Uppercase to Lowercase"
echo "2.Exit"
echo '___________________________________________'
echo -e "Enter Your Choice \c"
read ch
case "$ch" in
1) echo -e "Enter The Filename \c"
read f1
if [ -f $f1 ]
then
echo "Converting Uppercase to Lowercase"
tr '[A-Z]' '[a-z]' <$f1
else
echo "$f1 File Does't Exists"
fi ;;
2)
exit;;
esac
