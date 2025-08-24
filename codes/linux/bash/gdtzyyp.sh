# ----------------------------------------------------------------------------------------------------
# Title          : Bash shell script to print the current date and time
# File Name      : gdtzyyp.sh
# Compiled       : GNU bash, version 5.2.37(1)-release (x86_64-pc-linux-gnu)
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

#!/bin/bash

echo "———————————————————————————————————————————"
echo "Script to print the current date and time"
echo "———————————————————————————————————————————"
echo -n "Today's Date       | ";date
echo -n "Today's Day        | ";date +"%a"
echo -n "Today's Day        | ";date +"%A"
echo -n "Current Month      | ";date +"%b"
echo -n "Current Month      | ";date +"%B"
echo -n "Local Date & Time  | ";date +"%c"
echo -n "Date Of Month      | ";date +"%d"
echo -n "Date Of Month      | ";date +"%e"
echo -n "Today's Date       | ";date +"%D"
echo -n "Full Date(y-m-d)   | ";date +"%F"
echo -n "Last Digit Of Year | ";date +"%g"
echo -n "Year Of ISO Week No| ";date +"%G"
echo -n "Current Month      | ";date +"%h"
echo -n "Current Hour(00:23)| ";date +"%H"
echo -n "Current Hour(1:12) | ";date +"%I"
echo -n "Day Of Year(01-366)| ";date +"%j"
echo -n "Current Month      | ";date +"%m"
echo -n "Current Minute     | ";date +"%M"
echo -n "NanoSecond         | ";date +"%N"
echo -n "Now Time Is AM/PM  | ";date +"%p"
echo -n "Now Time Is am/pm  | ";date +"%P"
echo -n "12-Hour Clock Time | ";date +"%r"
echo -n "24-Hour Clock Time | ";date +"%R"
echo -n "Current Second     | ";date +"%S"
echo -n "Current Time       | ";date +"%T"
echo -n "Day Of Week(1-mon) | ";date +"%u"
echo -n "Local Date         | ";date +"%x"
echo -n "Local Time         | ";date +"%X"
echo -n "Last Digit Of Year | ";date +"%y"
echo -n "ISO Week Number    | ";date +"%V"
echo -n "Alphabet Time Zone | ";date +"%Z"
echo "———————————————————————————————————————————"
