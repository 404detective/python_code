#导入鸢尾花数据集、决策树分类器、计算交叉验证值的函数 cross_val_score
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
#使用默认参数，创建一颗基于基尼系数的决策树，并将该决策树分类器赋值给变量 clf
clf = DecisionTreeClassifier()
iris = load_iris()
'''
这里我们将决策树分类器做为待评估的模型，iris.data鸢尾花数据做为特征，
iris.target鸢尾花分类标签做为目标结果，通过设定cv为10，使用10折交叉验
证。得到最终的交叉验证得分。
'''
print(cross_val_score(clf, iris.data, iris.target, cv=10))
clf.fit(iris.data, iris.target)
print(clf.predict(iris.data))