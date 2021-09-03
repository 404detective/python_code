from sklearn.datasets import load_iris	
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
	

iris = load_iris()

# print(iris.keys())
# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])
# data：特征值 (数组) target：标签值 (数组) target_names：标签 (列表) DESCR：数据集描述 feature_names：特征 (列表) filename：iris.csv 文件路径

# n_samples, n_features = iris.data.shape	
# print((n_samples, n_features))	
# print(iris.feature_names)	
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# print(iris.data[0:5])
#  iris 数据中样本数量和特征的数量、特征名称和前五个示例

# print(iris.target.shape)	
# print(iris.target_names)	
# print(iris.target[0:5])
# 标签的大小、名称和前5个样本示例
# (150,) ['setosa' 'versicolor' 'virginica'] [0 0 0 0 0]

# iris_data = pd.DataFrame( iris.data, columns=iris.feature_names )	
# iris_data['species'] = iris.target_names[iris.target]	
# iris_data.head(3).append(iris_data.tail(3))

# print(iris_data)


from sklearn.linear_model import LinearRegression	
model = LinearRegression(copy_X=True,fit_intercept=True,n_jobs=None,normalize=True)

data=pd.read_csv('E:\Desktop\python_code\sklearn\dataset\liner.csv',sep=',')

x=np.array(data.x)
y=np.array(data.y)
# x = np.arange(10)
# y = 2 * x + 1
X = x[:, np.newaxis]
print(x)
print(X)
model.fit(X,y)

print( model.coef_ )	
print( model.intercept_ )

plt.scatter(x,y)
plt.plot([1],[1])
plt.show()