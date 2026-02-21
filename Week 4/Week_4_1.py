import pandas as pd
d = {
"Name": ["Tom", "James", "Ricky", "Vin", "Steve"],
"Age": [25, 26, 25, 23, 30],
"Rating": [4.23, 3.24, 3.98, 2.56, 3.20]
}
df = pd.DataFrame(d)
print(df.mean(numeric_only=True))