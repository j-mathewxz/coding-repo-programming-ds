import pandas as pd
import seaborn as sns

df = sns.load_dataset("tips")
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())

