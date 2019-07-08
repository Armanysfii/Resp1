import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

iris = load_iris()
x = iris.data

ms = MeanShift()
# bandwidth=5 increases cluster area
ms.fit(x)

labels = ms.labels_
centroids = ms.cluster_centers_

print(labels.shape)
plt.scatter(iris.data[:, 0], iris.data[:, 2], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 2], marker='X',
            s=180, linewidths=5)
# plt.show()
