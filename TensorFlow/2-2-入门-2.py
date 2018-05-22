import tensorflow as tf

state=tf.Variable(0,name='counter')#变量
one=tf.constant(1)#常量
new_value=tf.add(state,one)#定义一个op，state+1
update=tf.assign(state,new_value)#赋值OP，后面的赋值给前面一个

#init_op=tf.initialize_all_variables()
init=tf.global_variables_initializer()#需要将所有变量初始化

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(state))
    for _ in range(5):
        sess.run(update)
        print(sess.run(state))
