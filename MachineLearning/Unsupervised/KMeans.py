import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris = load_iris()
x = iris.data
kmn = KMeans(n_clusters=3)
kmn.fit(x)
labels = kmn.predict(x)

# print(labels)

centroids = kmn.cluster_centers_

# plt.scatter(iris.data[:, 0], iris.data[:, 2], c=labels)
# plt.scatter(centroids[:, 0], centroids[:, 2], marker='x', s=150, c='red')
# plt.show()
# print(kmn.inertia_)
list_inertia = []

for k in np.arange(1, 6):
    kmn = KMeans(n_clusters=k)
    kmn.fit(x)
    list_inertia.append(kmn.inertia_)

print(list_inertia)
plt.plot(np.arange(1,6), list_inertia, 'ro-')
plt.xlabel('number of clusters')
plt.ylabel('inertia')
plt.show()