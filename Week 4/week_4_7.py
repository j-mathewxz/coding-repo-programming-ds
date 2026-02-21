import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Create a moderately symmetric dataset (e.g., ages of a group)
np.random.seed(42) # for reproducibility
symmetric_data = np.random.normal(loc=30, scale=5, size=20).round(1)
# Ensure values are positive, relevant for 'age'
symmetric_data = symmetric_data[symmetric_data > 0]
df_symmetric = pd.DataFrame({'Value': symmetric_data})
print("Original Symmetric Dataset (first 5 rows):\n",
df_symmetric.head())
print("\n--- Initial Statistics ---")
print(f"Mean: {df_symmetric['Value'].mean():.2f}")
print(f"Median: {df_symmetric['Value'].median():.2f}")
print(f"Skewness: {df_symmetric['Value'].skew():.2f}")

df_high_outlier = df_symmetric.copy()
df_high_outlier.loc[len(df_high_outlier)] = 100 # Add a very high value
print("Dataset with High Outlier (last 5 rows):\n",
df_high_outlier.tail())
print("\n--- Statistics with High Outlier ---")
print(f"Mean: {df_high_outlier['Value'].mean():.2f}")
print(f"Median: {df_high_outlier['Value'].median():.2f}")
print(f"Skewness: {df_high_outlier['Value'].skew():.2f}")

# 3. Add a low outlier (reverting to original symmetric data first)
df_low_outlier = df_symmetric.copy()
df_low_outlier.loc[len(df_low_outlier)] = 5 # Add a very low value
print("Dataset with Low Outlier (last 5 rows):\n",
df_low_outlier.tail())
print("\n--- Statistics with Low Outlier ---")
print(f"Mean: {df_low_outlier['Value'].mean():.2f}")
print(f"Median: {df_low_outlier['Value'].median():.2f}")
print(f"Skewness: {df_low_outlier['Value'].skew():.2f}")


mu, sigma = 0.5, 0.1
s = np.random.normal(mu, sigma, 1000)
# Create the bins and histogram
count, bins, ignored = plt.hist(s, 20, density=True)
# Plot the distribution curve
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=3,
color='y')
plt.show()

