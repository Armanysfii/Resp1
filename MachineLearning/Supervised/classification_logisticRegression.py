import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import normalize

bcd = datasets.load_breast_cancer()
x = bcd.data
y = bcd.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

log = LogisticRegression()
log.fit(x_train, y_train)
y_pred = log.predict(x_test)

cm = confusion_matrix(y_test, y_pred, [0, 1])
cm = normalize(cm, norm='l1', axis=1)

df_cm = pd.DataFrame(cm, columns=bcd.target_names, index=bcd.target_names)
print(df_cm)












