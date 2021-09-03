import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_blobs
from sklearn.decomposition import PCA

from sklearn.datasets import load_iris
import pandas as pd
from pandas import DataFrame



iris = load_iris()
iris_X = iris.data   #x有4个属性，共有150个样本点
iris_y = iris.target #y的取值有3个，分别是0,1,2

pca = PCA(n_components=4)
pca.fit(iris_X)
#返回所保留的n个成分各自的方差百分比
print(pca.explained_variance_ratio_)
print(pca.explained_variance_)

pca1 = PCA(n_components=3)
pca1.fit(iris_X)
print(pca1.explained_variance_ratio_)
print(pca1.explained_variance_)

X_new = pca1.transform(iris_X)


# plt.scatter(X_new[:], X_new[:], marker='o',c=iris_y)
# plt.scatter(X_new[:, 0], X_new[:, 1], marker='o',c=iris_y)

fig = plt.figure()
ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=30, azim=20)
plt.scatter(X_new[:, 0], X_new[:, 1], X_new[:, 2], marker='o',c=iris_y)


plt.show()

# df_X = DataFrame(X_new, columns=['x1','x2'])
# df_y = DataFrame(iris_y, columns=['y'])
# df = pd.concat([df_X,df_y],axis=1)

# df0 = df[df.y==0]
# df1 = df[df.y==1]
# df2 = df[df.y==2]

# plt.scatter(df0.x1, df0.x2, color="r")
# plt.scatter(df1.x1, df1.x2, color="g")
# plt.scatter(df2.x1, df2.x2, color="b")

# plt.xlabel("x1")
# plt.ylabel("x2")
# plt.legend(labels = ["y0","y1","y2"],loc="best")
# plt.show()



# # X为样本特征，Y为样本簇类别， 共1000个样本，每个样本3个特征，共4个簇
# X, y = make_blobs(n_samples=10000, n_features=3, centers=[[3, 3, 3], [0, 0, 0], [1, 1, 1], [2, 2, 2]],
#                   cluster_std=[0.2, 0.1, 0.2, 0.2], random_state=9)
# fig = plt.figure()
# ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=30, azim=20)
# plt.scatter(X[:, 0], X[:, 1], X[:, 2], marker='o',c=y)
# plt.show()

# # pca = PCA(n_components=2)
# # pca = PCA(n_components=0.95)
# # pca = PCA(n_components=0.99)
# pca = PCA(n_components='mle', svd_solver='full')
# pca.fit(X)

# print(pca.explained_variance_ratio_)  
# # [0.98318212 0.00850037 0.00831751]
# print(pca.explained_variance_)  
# # [3.78521638 0.03272613 0.03202212]

# X_new = pca.transform(X)
# # plt.scatter(X_new[:, 0], X_new[:, 1], marker='o',c=y)
# plt.scatter(X_new[:], X_new[:], marker='o',c=y)
# plt.show()