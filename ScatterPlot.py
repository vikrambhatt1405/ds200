import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd

df = pd.read_csv('Working_Population_according_to_2011_Census.csv',header=None,names=['col1','col2','col3','col4','col5','col6','col7','col8','col9','col10','col11','col12','col13'])

df =  df.drop(df.index[[0,1]])

plt.scatter(df['col6'],df['col10'],color='#dd12dd',label="Male Vs Female Population")

plt.xticks(df['col6'],df['col6'],rotation='vertical')
#specifying labels
plt.xlabel("Male Population")
plt.ylabel("Female Population")
#enable legend
plt.legend()
plt.show()
