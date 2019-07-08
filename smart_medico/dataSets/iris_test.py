import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.linear_model import LinearRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

x = iris.data[:, np.newaxis,3]
y = iris.target
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3, random_state=42)
reg = LinearRegression()
reg.fit(xtrain, ytrain)
pred = reg.predict(xtest)

print("x train : ", xtrain.shape, "\n"
      , "x test : ", xtest.shape, "\n"
      , "y train : ", ytrain.shape, "\n"
      , "feature shape : ", y.shape, "\n"
      , "y test : ", ytest.shape)

plt.scatter(xtest, ytest)
plt.plot(xtest, pred)
plt.show()
