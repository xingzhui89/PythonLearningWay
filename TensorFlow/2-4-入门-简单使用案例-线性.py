import tensorflow as tf
import numpy as np

#使用numpy生成100个随机点
x_data=np.random.rand(100)
y_data=x_data*0.1+0.2

#构造一个线性模型
b=tf.Variable(0.)
k=tf.Variable(0.)
y=k*x_data+b

#二次代价函数
loss=tf.reduce_mean(tf.square(y-y_data))#求平方和的平均值

#定义一个梯度下降法来进行训练的优化器
optimizer=tf.train.GradientDescentOptimizer(0.2)#学习率是怎么确定的？

#最小化代价函数
train=optimizer.minimize(loss)

init=tf.global_variables_initializer()#对变量进行初始化

with tf.Session() as sess:
    sess.run(init)#首先要初始化
    for step in range(261):
        sess.run(train)
        if step%20==0:
            print(step,sess.run([k,b]))