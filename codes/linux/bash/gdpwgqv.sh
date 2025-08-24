# ----------------------------------------------------------------------------------------------------
# Title          : Bash shell script to calculate the area and circumference of a circle
# File Name      : gdpwgqv.sh
# Compiled       : GNU bash, version 5.2.37(1)-release (x86_64-pc-linux-gnu)
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

#!/bin/bash

echo "———————————————————————————————————————————"
echo "Script to calculate the area and circumference of a circle"
echo "———————————————————————————————————————————"
echo -n "Enter the radius of circle "
read RADIUS
PI=3.14159
AREA=$(echo "$PI*($RADIUS^2)"|bc)
CIRCUM=$(echo "(2*$PI*$RADIUS)"|bc)
echo "Area of a circle is $AREA"
echo "Circumference of a circle is $CIRCUM"
echo "———————————————————————————————————————————"
