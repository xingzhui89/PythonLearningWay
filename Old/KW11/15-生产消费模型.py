
#通过生成器实现协程并行运算

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield 1

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))
def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    print( c.__next__())
    print(c2.__next__())
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)

producer("alex")


# 协程究竟是个什么东西？
# Python对协程的支持是通过generator实现的。
#
# 在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。
#
# 但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。

# 我们再来看另外一个例子
def consumer():
    r = ''
    while True:
        n = yield r#这句很关键，n接受了从生产者那里传递的数值，然后返回了当前的r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'
def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)

# 注意到consumer函数是一个generator，把一个consumer传入produce后：
#
# 首先调用c.send(None)启动生成器；
#
# 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
#
# consumer通过yield拿到消息，处理，又通过yield把结果传回；
#
# produce拿到consumer处理的结果，继续生产下一条消息；
#
# produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
#
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。