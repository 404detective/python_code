import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv('dataset/x².csv',sep=',')

# print(data.x)
x=data.x
y=data.y
print(x.shape)
# x = x[:, np.newaxis]
# print(x.shape)
model=tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=1,input_shape=(1,)))
# model.summary()

adam=tf.keras.optimizers.Adam(learning_rate=0.04)

# lose_mse=tf.keras.losses.MSE(y,model.predict(x))
model.compile(optimizer=adam,loss='mse')

history=model.fit(x,y,batch_size=2,epochs=100)

w,b=model.layers[0].get_weights()

print('w=',w,'b=',b)

print(model.predict(x))

print(model.predict(pd.Series([2,5])))

plt.scatter(x,y)
plt.plot(x,model.predict(x))
plt.show()