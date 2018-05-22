'''
高阶函数定义:
1.函数接收的参数是一个函数名
2.函数的返回值是一个函数名
3.满足上述条件任意一个,都可称之为高阶函数
'''
# import time
# def foo():
#     time.sleep(3)
#     print('你好啊林师傅')
#
# def test(func):
#     # print(func)
#     start_time=time.time()#获取当前时间，记录下来
#     func()#执行传入的函数，请注意，如果不加括号，那么就是函数名，加括号才是执行
#     stop_time = time.time()
#     print('函数运行时间是  %s' % (stop_time-start_time))
# # foo()
# test(foo)#传入参数名，而不是传入一个执行函数

# def foo():
#     print('from the foo')
# def test(func):
#     return func#返回的是一个函数名

# res=test(foo)#res是一个函数名
# # print(res)
# res()#此时才是执行函数

# foo=test(foo)
# # # print(res)
# foo()

# import time
def foo():
    time.sleep(3)
    print('来自foo')

#不修改foo源代码
#不修改foo调用方式


#多运行了一次，不合格
# def timer(func):
#     start_time=time.time()
#     func()
#     stop_time = time.time()
#     print('函数运行时间是  %s' % (stop_time-start_time))
#     return func
# foo=timer(foo)
# foo()


#没有修改被修饰函数的源代码，也没有修改被修饰函数的调用方式，但是也没有为被修饰函数添加新功能
import time
def timer(func):
    start_time=time.time()
    return func# 这里设置return，下面的语句就不会被执行了
    stop_time = time.time()
    print('函数运行时间是  %s' % (stop_time-start_time))

foo=timer(foo)
foo()