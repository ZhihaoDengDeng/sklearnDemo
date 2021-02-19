# @Time : 2021/1/27 16:09
# @Author : DengZh
# @File : LinearRegressionDemo.py
# @Software: PyCharm

from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
 # y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 2])) + 3
reg = LinearRegression().fit(X, y)

print(reg.predict(np.array([[3,5]])))

