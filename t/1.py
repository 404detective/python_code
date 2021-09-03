import pandas
from sklearn.model_selection import train_test_split #交叉验证 训练和测试集合的分割
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# 读取csv数据
data = pandas.read_csv("E:/Desktop/python_code/t/data/liner.csv")

# 构建X和Y   scikit-learn要求X是一个特征矩阵，y是一个NumPy向量。pandas构建在NumPy之上。
# 因此，X可以是pandas的DataFrame，y可以是pandas的Series，scikit-learn可以理解这种结构
X = data[['x1','x2','x3','x4','x5']];  #返回 dataframe
print(type(X),"  ",X.shape);   # 返回X类型  X的维度
Y = data['y']; #返回Series类型  及list
print(type(Y),"   ",Y.shape);  # 返回X类型  X的维度

#  训练集测试集拆开 百分之75用于训练 百分之25用于测试
# random_state 在需要设置random_state的地方给其赋一个值，当多次运行此段代码能够得到完全一样的结果，别人运行此代码也可以复现你的过程。若不设置此参数则会随机选择一个种子，执行结果也会因此而不同了。虽然可以对random_state进行调参，但是调参后在训练集上表现好的模型未必在陌生训练集上表现好，所以一般会随便选取一个random_state的值作为参数。
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=1)
print(X_train.shape,"  ",X_test.shape,"  ",Y_train.shape,"  ",Y_test.shape)


# sklearn线性回归
lrg = LinearRegression()
model = lrg.fit(X,Y);  #训练
print(model)
print(lrg.intercept_);  #输出截距
coef = zip(['w1','w2','w3','w4','w5'],lrg.coef_) #特征和系数对应  打包对应为元组
for T in coef :
    print(T); #输出系数

#预测
y_pred = lrg.predict(X_test)
print(y_pred);  #输出测试值


plt.figure()
plt.plot(range(len(y_pred)),y_pred,'b',label="predict");   #x: x轴上的数值 y: y轴上的数值 ls：折线图的线条风格 lw：折线图的线条宽度 label：标记图内容的标签文本
plt.plot(range(len(Y_test)),Y_test,'r',label="test")
plt.xlabel("the number of sales")
plt.ylabel("value of sales")
plt.legend();  # 用于显示plot函数里面 label标签
plt.show()

