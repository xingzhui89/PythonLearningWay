import time
def timmer(func):#这是我们的装饰器，用来修饰其他函数的，参数是一个函数名
    #这个装饰器的作用应该就是记录函数func运行的时间
    def wrapper(*args,**kwargs):#传入的参数是list或者dict，或者说是任意参数
        start_time=time.time()
        res=func(*args,**kwargs)#函数参数运行
        stop_time = time.time()
        print('函数运行时间是%s' %(stop_time-start_time))
        return res#返回参数运行的结果
    #请注意，在time函数种，wrapper函数是没有运行的，只是一种修饰，用于返回
    return wrapper#返回修饰过的函数名

@timmer#常用的修饰方法，这样cal函数就被timmer所装饰，等价于cal=timmer(cal)
def cal(l):#cal函数的参数应该是个list或者某种序列
    res=0#结果的初始值
    for i in l:#遍历这个序列
        time.sleep(0.1)
        res+=i#对序列种的元素进行累计
    return res#遍历完成后返回

res=cal(range(20))#如果
print(res)