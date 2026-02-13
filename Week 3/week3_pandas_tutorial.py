import ssl
import certifi

ssl._create_default_https_context = lambda: ssl.create_default_context(
    cafile=certifi.where()
)

import pandas as pd
import seaborn as sns

df = sns.load_dataset("tips")
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())

df[['total_bill', 'tip', 'day', 'time']].head()
print(df)
df.iloc[0]
print(df.iloc[0])
df.iloc[10:20]
print(df.iloc[10:20])
df.loc[0:5, ['total_bill', 'tip']]
#print(df.iloc[0:5, ['total_bill', 'tip']])

last_5 = df.tail(5)
print(last_5)

subset = df.iloc[20:31][["total_bill", "size"]]
print(subset)

a = df[df['day'] == 'Sun']
print(a)
b= df[(df['day'] == 'Sun') & (df['total_bill'] > 20)]
print(b)

C = df.query("day == 'Sun' and total_bill > 20")
print(C)

dinner_expensive = df[(df["time"] == "Dinner") & (df["total_bill"] > 25)]

print(dinner_expensive)

count = dinner_expensive.shape[0]
print(count)

e = df.describe()
f = df.groupby('day')['tip'].mean()
g = df.groupby('sex')[['total_bill', 'tip']].mean()
print(e,f,g)

print(df.groupby("day")["tip"].mean().idxmax())
print(df.groupby("time")["total_bill"].mean().idxmax())