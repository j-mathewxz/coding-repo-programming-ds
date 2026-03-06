# -----------------------------
# Creating DataFrames
# -----------------------------

import pandas as pd
import numpy as np

# Using list
product_data = [['e-book', 2000], ['plants', 6000], ['Pencil', 3000]]
indexes = [1, 2, 3]
columns_name = ['product', 'unit_sold']

product_df = pd.DataFrame(data=product_data, index=indexes, columns=columns_name)
print(product_df)

# Using dictionaries
product_data = {
    'product': ['e-book', 'plants', 'Pencil'],
    'unit_sold': [2000, 5000, 3000]
}

product_df = pd.DataFrame(data=product_data)
print(product_df)

# Using numpy array
products = np.array([
    ['', 'product', 'unit_sold'],
    [1, 'E-book', 2000],
    [2, 'Plants', 6000],
    [3, 'Pencil', 3000]
])

product_pf = pd.DataFrame(
    data=products[1:, 1:],
    index=products[1:, 0],
    columns=products[0, 1:]
)

print(product_pf)  # same output as first case


# -----------------------------
# Reading CSV and Exploring Data
# -----------------------------

df = pd.read_csv('data/dirtydata.csv')

print(df.head(10))
print(df.info())
print(df.isna().sum())
print(df.duplicated())


# -----------------------------
# Dropping Missing Values
# -----------------------------

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())


# -----------------------------
# Filling Missing Values
# -----------------------------

df = pd.read_csv('data/dirtydata.csv')

df_new = df.fillna(130)

print(df_new.to_string())


# Fill missing values in specific column
df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace=True)


# Fill using mean
df = pd.read_csv('data.csv')

x = df["Calories"].mean()
df["Calories"].fillna(x, inplace=True)


# Fill using median
df = pd.read_csv('data.csv')

x = df["Calories"].median()
df["Calories"].fillna(x, inplace=True)


# Fill using mode
df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace=True)


# -----------------------------
# Date Conversion
# -----------------------------

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())


# -----------------------------
# Removing rows with missing Date
# -----------------------------

df.dropna(subset=['Date'], inplace=True)


# -----------------------------
# Fixing incorrect values
# -----------------------------

df.loc[7, 'Duration'] = 45


# Replace values greater than 120
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120


# Remove rows with Duration > 120
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)


# -----------------------------
# Checking duplicates
# -----------------------------

print(df.duplicated())


# -----------------------------
# Removing duplicates
# -----------------------------

df.drop_duplicates(inplace=True)