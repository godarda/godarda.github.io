# ----------------------------------------------------------------------------------------------------
# Title          : Python Pandas to create a bar graph using the matplotlib module
# File Name      : gdleovy.py
# Compiled       : Python 3.13.3
# Author         : GoDarda
# License        : GNU General Public License
# ----------------------------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plot
df=pd.read_csv("/home/godarda/gd.csv")

x=df['account_no']
y=df['amount']

plot.bar(x,y, label="Bank Holders")
plot.xlabel("Account Numbers")
plot.ylabel("Current Amount")

plot.title("New Bank Holders")
plot.show()
