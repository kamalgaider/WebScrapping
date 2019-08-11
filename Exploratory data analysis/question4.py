import numpy as np
import pandas as pd

df = pd.read_csv("../CSV_without_comments.csv", sep=',')
fltr = df['Genre'] =='Classics'
df.where(fltr, inplace = True)
df = df.dropna()
print('Range : ' + str(df['Star Rating'].max() - df['Star Rating'].min()))



