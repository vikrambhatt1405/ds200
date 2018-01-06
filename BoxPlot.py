import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np
df = pd.read_csv('Working_Population_according_to_2011_Census.csv',header=None,names=['col1','col2','col3','col4','col5','col6','col7','col8','col9','col10','col11','col12','col13'])

df =  df.drop(df.index[[0,1]])

plotMap=[]

plotMap.append(np.array(df['col2']).astype(np.float).tolist())
plotMap.append(np.array(df['col6']).astype(np.float).tolist())
plotMap.append(np.array(df['col10']).astype(np.float).tolist())

plt.boxplot(plotMap)

plt.xticks([1,2,3],["Total Population","Male Population","Female Population"])
plt.ylabel("Population in Billions")
plt.title("Working population according to 2011 census")
plt.legend()
plt.show()
