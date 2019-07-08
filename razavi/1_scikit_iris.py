from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt

iris = load_iris()

# print(iris.data[0])
# print(np.unique(iris.target, return_counts=True)) # target values
# print(iris.target_names) # target names
x_index = 3
colors = ["blue", "red", "green"]
for label, color in zip(range(len(iris.target_names)), colors):
    plt.hist(iris.data[iris.target==label, x_index],
             label=iris.target_names[label],
             color=color)
plt.xlabel(iris.feature_names[x_index])
plt.legend() 
plt.show()