import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn import datasets

iris = datasets.load_iris()
# print(iris.data.shape , "\n",
#       iris.target_names, "\n",
#       iris.feature_names, "\n",
#       iris)

df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
df_iris['target'] = iris.target
# print(df_iris)

# visual EDA
scatter_matrix(df_iris, figsize=[11, 11], c=iris.target)
plt.show()
