import numpy as np
import pandas as pd

df = pd.read_csv("../CSV_without_comments.csv", sep=',')
#print(df.Genre.unique())
#print(len(df.Genre.unique()))
df = df.drop_duplicates()
print(len(df.Author.unique()))
#print(df.groupby('Author')['Genre'].value_counts())
print(df.groupby(['Author','Genre']).size())