# E:\Desktop\python_code\sklearn\课程数据\聚类\31省市居民家庭消费水平-city.txt

import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import sklearn
import numpy as np
# X为样本特征，Y为样本簇类别，共1000个样本，每个样本2个特征，对应x和y轴，共4个簇，
# 簇中心在[-1,-1], [0,0],[1,1], [2,2]， 簇方差分别为[0.4, 0.2, 0.2]


def loadData(filePath):
    fr = open(filePath,'r+')
    lines = fr.readlines()
    retData = []
    retCityName = []
    for line in lines:
        items = line.strip().split(",")
        retCityName.append(items[0])
        retData.append([float(items[i])
    for i in range(1 ,len(items))])
    return retData,retCityName

data,city=loadData("E:\Desktop\python_code\sklearn\课程数据\聚类\city.txt")
# print(data,city)
# y_pred = KMeans(n_clusters=4).fit_predict(data)
km=KMeans(n_clusters=4)
y_pred = km.fit_predict(data)
expenses = np.sum(km.cluster_centers_,axis=1)
# print(expenses)
CityCluster = [[],[],[],[]]
for i in range(len(city)):
    CityCluster[y_pred[i]].append(city[i])
for i in range(len(CityCluster)):
    print("Expenses:%.2f" % expenses[i])
    print(CityCluster[i])


# X, y = make_blobs(n_samples=500, n_features=2 , centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],
#                   cluster_std=[0.7, 0.7, 0.7, 0.7], random_state=10)
# print(X)
# print(y)   

# y_pred = KMeans(n_clusters=4).fit_predict(X)
# print(sklearn.metrics.calinski_harabasz_score(X, y_pred))
# plt.figure(figsize=(12, 6))
# plt.subplot(121)
# plt.xlim((-3,3))
# plt.ylim((-3,3))
# plt.xlabel('X1')
# plt.ylabel('X2')
# plt.scatter(X[:, 0], X[:, 1], c=y_pred)

# plt.subplot(122)
# plt.xlim((-3,3))
# plt.ylim((-3,3))
# plt.xlabel('X1')
# plt.ylabel('X2')
# # print(np.ones(500))
# plt.scatter(X[:, 0], X[:, 1], c=y_pred)

# plt.show()





# #首先绘制点的分布：
# ax2.scatter(x[:,0],x[:,1]
#             ,marker="o"
#             ,s=8
#             ,c=colors
#             )
# #把质心放入图片：
# centers = clusterer.cluster_centers_

# ax2.scatter(centers[:,0],centers[:,1]
#             ,marker="x"
#             ,c="red"
#             ,alpha=1
#             ,s=200
#             )
# ————————————————
# 版权声明：本文为CSDN博主「天甜费，」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_46008828/article/details/114296785







# print(__doc__)

# Author: Phil Roth <mr.phil.roth@gmail.com>
# License: BSD 3 clause

# import numpy as np
# import matplotlib.pyplot as plt

# from sklearn.cluster import KMeans
# from sklearn.datasets import make_blobs

# plt.figure(figsize=(12, 12))

# n_samples = 1500
# random_state = 170
# X, y = make_blobs(n_samples=n_samples, random_state=random_state)

# # Incorrect number of clusters
# y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X)

# plt.subplot(221)
# plt.scatter(X[:, 0], X[:, 1], c=y_pred)
# plt.title("Incorrect Number of Blobs")

# # Anisotropicly distributed data
# transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
# X_aniso = np.dot(X, transformation)
# y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_aniso)

# plt.subplot(222)
# plt.scatter(X_aniso[:, 0], X_aniso[:, 1], c=y_pred)
# plt.title("Anisotropicly Distributed Blobs")

# # Different variance
# X_varied, y_varied = make_blobs(n_samples=n_samples,
#                                 cluster_std=[1.0, 2.5, 0.5],
#                                 random_state=random_state)
# y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_varied)

# plt.subplot(223)
# plt.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
# plt.title("Unequal Variance")

# # Unevenly sized blobs
# X_filtered = np.vstack((X[y == 0][:500], X[y == 1][:100], X[y == 2][:10]))
# y_pred = KMeans(n_clusters=3,
#                 random_state=random_state).fit_predict(X_filtered)

# plt.subplot(224)
# plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
# plt.title("Unevenly Sized Blobs")

# plt.show()