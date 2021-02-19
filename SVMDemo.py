# @Time : 2021/1/27 16:31
# @Author : DengZh
# @File : SVMDemo.py
# @Software: PyCharm

import numpy as np
from sklearn.svm import SVR

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 2])) + 3

# model = SVR()
#调参 高斯核作为它的核函数，同时将核参数设为1，惩罚系数设为100
#调参后的svm模型
model = SVR(kernel='rbf',gamma=1,C=100)
model.fit(X, y)
print(model.predict(X))
