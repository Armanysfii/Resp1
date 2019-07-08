from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
x, y = iris.data, iris.target
model = KNeighborsClassifier()

x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                    test_size=0.5,
                                                    random_state=42,
                                                    stratify=y)
# print(x_train.shape)
# print(x_test.shape)
# print(y_train.shape)
# print(y_test.shape)

labels, counts = np.unique(y,
                           return_counts=True)
print(counts / float(len(y)))

model.fit(x_train, y_train)
y_pred = model.predict(x_test)
test_accuracy = accuracy_score(y_test, y_pred)
print(y_test,"\n",y_pred)

plt.figure(figsize=(10, 6))
colors = ["darkblue", "darkgreen", "gray"]
for n, color in enumerate(colors):
    idx = np.where(y_test == n)[0]
    plt.scatter(x_test[idx, 1], x_test[idx, 2], c=color, label="class %s"%str)
plt.scatter(x_test[incorrect_idx, 1], x_test[incorrect_idx, 2], c="darkred")

plt.xlabel("sepal width [cm]")
plt.ylabel("petal width [cm]")
plt.legend()
plt.title("iris classification result")
plt.show()