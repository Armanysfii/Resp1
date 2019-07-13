import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

x, y = make_blobs(random_state=42)
print(x.shape)
model = KMeans(n_clusters=3, random_state=42)
labels = model.fit_predict(x)

# plt.scatter(x[:, 0], x[:, 1], c=labels)
# plt.show()

distortions = list()
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(x)
    distortions.append(kmeans.inertia_)

plt.plot(range(1,11), distortions, marker="o")
plt.xlabel("number of clusters")
plt.ylabel("distortion")
plt.show()