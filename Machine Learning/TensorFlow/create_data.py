import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

path='E:/Desktop/python_code/Machine Learning/TensorFlow/dataset/'
x=np.random.uniform(-100,100,(100,))
# 一开始写成了(100.1) 它的ndim为2 二维数组 不能跟一维数组绘制图表
print(x)
c=np.random.uniform(-1000,1000,(100,))

# print(x.shape,x.ndim)
# print(c.shape,c.ndim)
y=x*x+2*c

df=pd.DataFrame({'x':x,'y':y})

df.to_csv(path+'x².csv')

# print(len(x))
# print(len(c))
# print(len(y))
plt.scatter(x,y)
plt.show()