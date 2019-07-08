import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import load_iris

iris = load_iris()
x = iris.data

# eps : kmtar beshe shoae dide data kamtar mishe , noise bishtar mishe
# min_sample :

dbscan = DBSCAN(eps=0.5)
dbscan.fit(x)
labels = dbscan.labels_
# [-1] = noise

plt.scatter(x[:, 0], x[:, 2], c=labels)
plt.show()
# sci_pub