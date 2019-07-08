import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

x, y = make_blobs(centers=2, random_state=0, cluster_std=1.5)

plt.figure(figsize=(10, 6))
plt.scatter(x[y == 0, 0], x[y == 0,1], c="blue", s=40, label="0")
plt.scatter(x[y == 1, 0], x[y == 1,1], c="red", s=40, label="1", marker="s")

plt.xlabel("first feature")
plt.ylabel("second feature")
plt.legend()
plt.show()
