import ssl
import certifi

ssl._create_default_https_context = lambda: ssl.create_default_context(
    cafile=certifi.where()
)

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
print(df.head())

print(df.shape)
print(df.columns)
print(df.head())

print(df.isnull().sum())
# Show only columns that have missing data
missing_columns = df.isnull().sum()[df.isnull().sum() > 0]
print(missing_columns)

# Fill missing age with median
df["age"] = df["age"].fillna(df["age"].median())

# Fill missing embarked with mode
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

# Drop deck column
df.drop(columns=["deck"], inplace=True)

# Optional: check missing values again
print(df.isnull().sum())

# 1) Survival rate by sex
print(df.groupby('sex')['survived'].mean())

# 2) Survival rate by class
print(df.groupby('class')['survived'].mean())

# 3) Survival rate by embark_town
print(df.groupby('embark_town')['survived'].mean())

# 1) How many passengers were female AND in first class
female_first = df[(df['sex'] == 'female') & (df['class'] == 'First')]
print("Female & First Class:", len(female_first))

# 2) Survival rate of children (age < 16)
children = df[df['age'] < 16]
print("Children survival rate:", children['survived'].mean())

# 3) Survival rate of males in third class
male_third = df[(df['sex'] == 'male') & (df['class'] == 'Third')]
print("Males in Third Class survival rate:", male_third['survived'].mean())

# Create age_group column
df['age_group'] = df['age'].apply(lambda x: 'child' if x < 16 else 'adult')

# Compute survival rate by age_group
print(df.groupby('age_group')['survived'].mean())

summary = df.groupby(['class', 'sex']).agg(
    passenger_count=('survived', 'count'),
    survival_rate=('survived', 'mean')
).reset_index()

# Sort by survival rate descending
summary_sorted = summary.sort_values(by='survival_rate', ascending=False)
print(summary_sorted)

final_report = summary_sorted[['sex', 'class', 'passenger_count', 'survival_rate']]
print(final_report)