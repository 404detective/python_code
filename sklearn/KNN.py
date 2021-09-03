from sklearn.neighbors import KNeighborsClassifier
#创建一组数据 X 和它对应的标签 y
X=[[0],[1],[2],[3]]
y=[0,1,2,3]
#使用最近的3个邻居作为分类的依据，得到分类器
neigh = KNeighborsClassifier(n_neighbors=1)
#将训练数据 X 和 标签 y 送入分类器进行学习
neigh.fit(X, y)
#调用 predict() 函数，对未知分类样本 [1.1] 分类，可以直接并将需要分类
#的数据构造为数组形式作为参数传入，得到分类标签作为返回值
print(neigh.predict([[2.2],[2.3],[2.6]]))