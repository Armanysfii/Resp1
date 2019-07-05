import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report

bcd = datasets.load_breast_cancer()
x = bcd.data
y = bcd.target
# print(x.shape, bcd.target_names, y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
# print(y_pred)

# hamishe labele aval positive e
print(confusion_matrix(y_test, y_pred, [0, 1]))
print(classification_report(y_test, y_pred))










