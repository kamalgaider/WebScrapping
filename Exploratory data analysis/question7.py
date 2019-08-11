import numpy as np
import pandas as pd

df = pd.read_csv("../CSV_without_comments.csv", sep=',')
fltr = df['Genre'] =='Business'
df.where(fltr, inplace = True)
df = df.dropna()
print(df.loc[:,'Star Rating'].std())



