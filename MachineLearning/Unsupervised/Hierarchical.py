import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

# linkage : methode cluster

iris = load_iris()
hierarchical = linkage(iris.data, method='complete')
# dendrogram(hierarchical)
# plt.show()

# level of clusters
labels = fcluster(hierarchical, 6, criterion='distance')
plt.scatter(iris.data[:, 0], iris.data[:, 2], c=labels)
plt.show()
