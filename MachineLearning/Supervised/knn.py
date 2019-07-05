import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)

# x = iris.data[:, [2, 3]]
# y = iris.target # use for 3types of color in plot
# print(x[2],y[2])

# plt.scatter(x[:, 0], x[:, 1], c=y)
# plt.show()


knn = KNeighborsClassifier(n_neighbors=6, metric='minkowski', p=2)

x = iris.data
y = iris.target

print(knn.fit(x, y))

x_new = np.array([[5, 3, 1, 0.2]])
y_new = knn.predict(x_new)

print(y_new)  # output is 0 : SETOSA iris flower

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42, stratify=y)
# test_size : chan darsad az etelaat baraye test ya train bashe , bishtar baraye train negah dashte mishe 30%
# random_state : tolide adade tasadofi
# stratify : tuye etelaate train o test be hamun nesbate barchasb ha hastan etelaat o joda mikone

print(x_train.shape, "datas for train part")
print(x_test.shape, "datas for test part")

###### EVALUATION MODEL

knn1 = KNeighborsClassifier(n_neighbors=6)
knn1.fit(x_train, y_train)
y_predict = knn1.predict(x_test)
# print(knn1.score(x_test, y_test))

# preallocate

neighbors = np.arange(1, 30)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

for i, k in enumerate(neighbors):
    knn_model = KNeighborsClassifier(n_neighbors=k)
    knn_model.fit(x_train, y_train)
    train_accuracy[i] = knn_model.score(x_train, y_train)
    test_accuracy[i] = knn_model.score(x_test, y_test)

plt.plot(neighbors, train_accuracy, label='train accuracy')
plt.plot(neighbors, test_accuracy, label='test accuracy')
plt.legend()
plt.xlabel('accuracy')
plt.ylabel('number of neighbors')
plt.show()






