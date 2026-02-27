import os
import pandas as pd
sample_data_path = "C:/Users/gopal/PycharmProjects/Quant/data"
files = [os.path.join(sample_data_path, f) for f in os.listdir(sample_data_path) if
f.endswith(".csv")]
dfs = [pd.read_csv(file) for file in files]
# Check if the dfs list is not empty before attempting to concatenate
if dfs:
    combined = pd.concat(dfs)
    print(combined)
else:
print("No CSV files found in the directory to concatenate.")