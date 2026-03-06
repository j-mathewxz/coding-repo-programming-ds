import matplotlib
print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from numpy import random

# Line plot
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints)
plt.show()

# Simple plot
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()

# Plot with markers
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker='o')
plt.show()

# Sports watch example
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()

# Subplots example
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2,1,1)
plt.plot(x,y)

plt.subplot(2,1,2)
plt.plot(x,y)

plt.show()

# Scatter plot
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x,y,color='hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

plt.scatter(x,y,color='#88c999')
plt.show()

# Scatter with color scale
colors = np.array([0,10,20,30,40,45,50,55,60,70,80,90,100])
plt.scatter(x[:13], y[:13], c=colors, cmap='viridis')
plt.colorbar()
plt.show()

# Bar chart
x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

plt.bar(x,y,color="red")
plt.show()

# Histogram
x = np.random.normal(170,10,250)
plt.hist(x)
plt.show()

# Pie chart
y = np.array([35,25,25,15])
labels = ["Apples","Bananas","Cherries","Dates"]

plt.pie(y, labels=labels)
plt.legend(title="Four Fruits:")
plt.show()

# Seaborn distribution plot
sns.histplot(random.normal(size=1000), kde=True)
plt.show()

# Seaborn lineplot using iris dataset
data = sns.load_dataset("iris")

sns.lineplot(x="sepal_length", y="sepal_width", data=data)
plt.show()

# Seaborn subplots
def graph():
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)

plt.subplot(121)
graph()

plt.subplot(122)
graph()

plt.show()

# FacetGrid
plot = sns.FacetGrid(data, col="species")
plot.map(plt.plot, "sepal_width")
plt.show()

# PairGrid
data2 = sns.load_dataset("flights")
plot = sns.PairGrid(data2)
plot.map(plt.plot)
plt.show()

# Barplot
sns.barplot(x='species', y='sepal_length', data=data)
plt.show()

# Boxplot
sns.boxplot(x='species', y='sepal_width', data=data)
plt.show()

# Pairplot
sns.pairplot(data=data, hue='species')
plt.show()

# Heatmap
data3 = sns.load_dataset("tips")
tc = data3.corr()
sns.heatmap(tc)
plt.show()