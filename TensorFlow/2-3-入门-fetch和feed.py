import tensorflow as tf

#Fetch的概念，在会话中同时执行多个op，得到运行结果
# input1=tf.constant(3.0)
# input2=tf.constant(2.0)
# input3=tf.constant(5.0)
#
# add=tf.add(input2,input3)#求和
#
# mul=tf.multiply(input1,add)#乘法
#
# with tf.Session() as sess:
#     result=sess.run([mul,add])
#     print(result)

#Feed的概念
#创建占位符，用处？
input1=tf.placeholder(tf.float32)
input2=tf.placeholder(tf.float32)

output=tf.multiply(input1,input2)

with tf.Session() as sess:
    #feed的数据以字典的形式传入，给前面的占位符赋值
    print(sess.run(output,feed_dict={input1:[7.],input2:[2.]}))
