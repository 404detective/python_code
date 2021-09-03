#房价与房屋尺寸关系的线性拟合（线性回归）
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

#画图时有中文需要设置字体
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
#设置自变量和因变量
data_x=[] #设房屋的尺寸（面积）为data_x
data_y=[] #房价为data_y
#读取数据
f=open('E:\Desktop\python_code\sklearn\课程数据\回归\prices.txt','r') #自己存放的数据位置
lines=f.readlines()
for line in lines:
    items=line.strip().split(',')  #line.去掉(空格).分割(',')
    data_x.append(int(items[0]))
    data_y.append(int(items[1]))
length=len(data_x)
data_x=np.array(data_x).reshape(length,1) #自变量x 
data_y=np.array(data_y)   #因变量y
minX=min(data_x)
maxX=max(data_x)
x=np.arange(minX,maxX).reshape([-1,1])
linear=linear_model.LinearRegression()  # sklearn 里有线性模型
linear.fit(data_x,data_y)  #拟合x，y

# print ("training set score:{:.2f}".format(linear.score(X_train,y_train)))
# print ("test set score:{:.2f}".format(linear.score(X_test,y_test)))

print('Coefficients:',linear.coef_)   #线性系数
print('intercept:',linear.intercept_)  #与y轴的交点坐标
plt.scatter(data_x,data_y,color='green') #散点图
plt.plot(x,linear.predict(x),color='blue') 
plt.xlabel('Area')  #x轴标签
plt.ylabel('Price')
plt.title('房价与房屋尺寸关系的线性关系图')
plt.show()















# from sklearn import linear_model        #表示，可以调用sklearn中的linear_model模块进行线性回归。
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# print(x,y)
# model = linear_model.LinearRegression()
# model.fit(x.reshape(-1,1), y.reshape(-1,1))
# print(model.intercept_)  #截距
# print(model.coef_)  #线性模型的系数
