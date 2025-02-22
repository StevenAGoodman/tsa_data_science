import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

sns.set_theme(style="white")

df = pd.read_csv("./input.csv")

print(df.head())

sns.pairplot(df)

plt.figure()
df_num = df.select_dtypes("number").corr()
cmap = sns.diverging_palette(230, 20, as_cmap=True)
mask = np.triu(np.ones_like(df_num, dtype=bool))

sns.heatmap(df_num, mask=mask, cmap=cmap)

plt.show()
