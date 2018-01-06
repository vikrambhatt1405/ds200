import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np

df = pd.read_csv('Estimated_Population_of_Haryana_1961-2011.csv',header = None,names = ['col1','col2'])

df = df.drop(df.index[[0,45]]).drop(57)

plt.bar(df['col1'],np.array(df['col2']).astype(np.float))
plt.xticks(rotation='vertical')
plt.xlabel("Year")
plt.ylabel("Population")
plt.title('Estimated Population of Haryana')
plt.legend()
plt.show()

