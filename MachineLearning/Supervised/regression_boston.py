import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

boston = load_boston()
df_boston = pd.DataFrame(boston.data, columns=boston.feature_names)
df_boston['Price'] = boston.target

# print(df_boston.head(10))

x = boston.data
y = boston.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

reg = LinearRegression()
reg.fit(x_train, y_train)
y_predict = reg.predict(x_test)

plt.scatter(y_test, y_predict)
plt.ylabel("prices")
plt.xlabel("predicted prices")
# plt.show()


# age azin meqdar jazr begirim rmse bedast miad
# ke harcchi nazdiktar be 0 bashe yani modele behtari darim
mse = mean_squared_error(y_test, y_predict)
print(mse)

new_x = boston.data[:, [1, 2]]
new_y = boston.target

new_x_train, new_x_test, new_y_train, new_y_test = train_test_split(new_x, new_y, test_size=0.3, random_state=42)
new_reg = LinearRegression()
new_reg.fit(new_x_train, new_y_train)

new_y_predict = new_reg.predict(new_x_test)

new_mse = mean_squared_error(new_y_test, new_y_predict)
print(new_mse)
