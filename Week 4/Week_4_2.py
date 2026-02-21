import pandas as pd
#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
'Lee','Chanchal','Gasper','Naviya','Andres']),
'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
#Create a DataFrame
df = pd.DataFrame(d)
print ("Mean Values in the Distribution")
# Select only numeric columns for mean calculation
print(df.mean(numeric_only=True))
print ("*******************************")
print ("Median Values in the Distribution")
# Select only numeric columns for median calculation
print(df.median(numeric_only=True))

