import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

data = load_boston()

x = data.data
y = data.target

reg = LinearRegression()
cv_scores = cross_val_score(reg, x, y, cv=5)
# cv attribute is the K
print(cv_scores)
print(np.mean(cv_scores))