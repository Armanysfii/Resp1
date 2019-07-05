import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import Lasso

data = load_boston()
x = data.data
y = data.target

lasso = Lasso(alpha=0.1, normalize=True)
lasso.fit(x, y)
lasso_coeff = lasso.coef_

print(lasso_coeff)
plt.plot(range(13), lasso_coeff)
plt.xticks(range(13), data.feature_names)
plt.ylabel('coefficents')
plt.show()
