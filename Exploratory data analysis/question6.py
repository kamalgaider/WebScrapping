import numpy as np
import pandas as pd

df = pd.read_csv("../CSV_without_comments.csv", sep=',')

df = df.dropna()
df = df.loc[df['Star Rating'].idxmax()]
print(df)




