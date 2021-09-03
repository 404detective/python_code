import sklearn.decomposition as dp
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from numpy.random import RandomState #创建随机种子
n_row,n_col=2,3
n_components=n_row*n_col
image_shape=(64,64)
datasets=fetch_olivetti_faces(shuffle=True,random_state=RandomState(0))
#dataset=fetch_olivetti_faces(data_home=None,shuffle=False,random_state=0,download_if_missing=True)
faces=datasets.data #加载工打开数据

def plot_gallery(title,images,n_col=n_col,n_row=n_row):
    plt.figure(figsize=(2.*n_col,2.26*n_row)) #创建图片，并指定图片大小
    plt.suptitle(title,size=18) #设置标题及字号大小
    
    for i,comp in enumerate(images):
        plt.subplot(n_row,n_col,i+1) #选择绘制的子图
        vmax=max(comp.max(),-comp.min())
        
        plt.imshow(comp.reshape(image_shape),cmap=plt.cm.gray,
                   interpolation='nearest',vmin=-vmax,vmax=vmax) #对数值归一化，并以灰度图形式显示
        plt.xticks(())
        plt.yticks(()) #去除子图的坐标轴标签
    plt.subplots_adjust(0.01,0.05,0.99,0.94,0.04,0.) #对子图位置及间隔调整

plot_gallery('First centered Olivetti faces',faces[:n_components])
estimators=[
        ('Eigenfaces-PCA using randomized SVD',
         dp.PCA(n_components=6,whiten=True)),
         ('Non-negative components - NMF',
          dp.NMF(n_components=6,init='nndsvda',
                            tol=5e-3))] #NMF和PCA实例化

for name,estimator in estimators: #分别调用PCA和NMF
    estimator.fit(faces) #调用PCA或NMF提取特征
    components_=estimator.components_ #获取提取的特征
    plot_gallery(name,components_[:n_components]) #按照固定格式进行排列
plt.show()


























# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from sklearn.datasets import make_blobs

# from sklearn.decomposition import NMF
# from sklearn.datasets import load_iris



# iris = load_iris()
# iris_X = iris.data   #x有4个属性，共有150个样本点
# iris_y = iris.target #y的取值有3个，分别是0,1,2

# NMF = NMF(n_components=2)
# NMF.fit(iris_X)

# X_new = NMF.transform(iris_X)

# # plt.scatter(X_new[:], X_new[:], marker='o',c=iris_y)

# plt.scatter(X_new[:, 0], X_new[:, 1], marker='o',c=iris_y)

# # fig = plt.figure()
# # ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=30, azim=20)
# # plt.scatter(X_new[:, 0], X_new[:, 1], X_new[:, 2], marker='o',c=iris_y)


# plt.show()