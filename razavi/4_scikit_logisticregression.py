import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs


x, y = make_blobs(centers=2, random_state=0, cluster_std=1)
x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                    test_size=0.3,
                                                    random_state=0)
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

# print(y_pred)
# print(y_test)

print(np.mean(y_pred == y_test))
# or
print(model.score(x_test, y_test))

plt.scatter(x[y == 0, 0], x[y == 0,1], c="blue", s=40, label="0")
plt.scatter(x[y == 1, 0], x[y == 1,1], c="red", s=40, label="1", marker="s")
plt.xlabel("first feature")
plt.ylabel("second feature")
# plt.plot(model, x_train)
plt.legend()
plt.show()
