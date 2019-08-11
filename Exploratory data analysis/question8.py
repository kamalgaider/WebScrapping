import numpy as np
import pandas as pd

df = pd.read_csv("../CSV_without_comments.csv", sep=',')
df = df.loc[df['Number of Votes'].idxmax()]
print(df)




