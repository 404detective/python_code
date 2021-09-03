#房价与房屋尺寸关系的非线性拟合（多项式回归）
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
data_x=[]
data_y=[] 
f=open('E:\Desktop\python_code\sklearn\课程数据\回归\prices.txt','r')
lines=f.readlines()
for line in lines:
    items=line.strip().split(',')  #line.去掉(空格).分割(',')
    data_x.append(int(items[0]))
    data_y.append(int(items[1]))
length=len(data_x)
data_x=np.array(data_x).reshape([length,1])
data_y=np.array(data_y)
minX=min(data_x)
maxX=max(data_x)
x=np.arange(minX,maxX).reshape([-1,1])

poly_reg=PolynomialFeatures(degree=2) #degree=2表示建立data_x的二次多项式特征X_poly
x_poly=poly_reg.fit_transform(data_x)

linear=linear_model.LinearRegression()
linear.fit(x_poly,data_y)  #拟合x，y

plt.scatter(data_x,data_y,color='green')
plt.plot(x,linear.predict(poly_reg.fit_transform(x)),color='blue')
plt.xlabel('Area')  #x轴标签
plt.ylabel('Price')
plt.title('房价与房屋尺寸关系的一元二次多项式拟合关系图')
plt.show()
