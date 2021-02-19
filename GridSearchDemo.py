# @Time : 2021/1/27 20:16
# @Author : DengZh
# @File : GridSearchDemo.py
# @Software: PyCharm
#网格交叉验证调参，以SVR为例
from sklearn import svm,datasets
from sklearn.model_selection import GridSearchCV
irisDB=datasets.load_iris()
parameters={'kernel':('linear','rbf'),'C':[1,10]}
svc=svm.SVC()
clf=GridSearchCV(svc,parameters)
clf.fit(irisDB.data,irisDB.target)
#穷举网格中表现性能最好的一组参数
print(clf.best_params_)
#穷举表现最好的一个模型
#clf.best_estimator
# GridSearchCV(estimator=svc(),param_grid={'C'=[1,10],'kernel':('linear','rbf')})
# print(sorted(clf.cv_results_.keys()))