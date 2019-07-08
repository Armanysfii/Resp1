from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data = load_diabetes()

# TODO

x = data.data[:, np.newaxis, 3]  # specific data

# x = data.data # all data ...

y = data.target

df_hd = pd.DataFrame(data.data, columns=data.feature_names)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

reg = LinearRegression()
reg.fit(x_train, y_train)
pred = reg.predict(x_test)

# info about dataSet

print("Dataframe shape", df_hd.shape, "\n"
      , "x train : ", x_train.shape, "\n"
      , "x test : ", x_test.shape, "\n"
      , "y train : ", y_train.shape, "\n"
      , "feature shape : ", y.shape, "\n"
      , "predict shape : ", pred.shape, "\n"
      , "y test : ", y_test.shape)
print(df_hd.iloc[0])
# print(data.feature_names)

# x_shaped = x_test.reshape(1000, 100)
# y_shaped = y_train.reshape(1000, 100)


# TODO

# plt.scatter(x_test, y_test, c="r")

plt.plot(x_test, pred)
plt.xlabel('X text')
plt.ylabel('predict')
plt.show()
