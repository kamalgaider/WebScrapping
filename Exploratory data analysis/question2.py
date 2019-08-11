import numpy as np
import pandas as pd

df = pd.read_csv("../CSV_without_comments.csv", sep=',')
#print(df.head(5))
#print(df.dtypes)
#print(df.shape)
#print(df[df.duplicated()].shape)
df = df.drop_duplicates()
#print(df.shape)
#print(df.isnull().sum())
#print(df.count())
print(df[df.Genre == 'Science Fiction'].count())