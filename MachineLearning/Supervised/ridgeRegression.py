import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

data = load_boston()
x = data.data
y = data.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)


ridge = Ridge(alpha=0.1, normalize=True)
ridge.fit(x_train, y_train)
ridge_predict = ridge.predict(x_test)

plt.scatter(ridge_predict, y_test)
plt.ylabel('prices')
plt.show()
