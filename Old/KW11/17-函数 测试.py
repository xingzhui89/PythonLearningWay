# 第一个测试
def func(start,end,a=0,b=0):
    if start == end:
        return a,b
    if start%3 == 0 and end%7 == 0:
        a +=1
        b += start
    ret = func(start+1,end,a,b)
    return ret#虽然是return，但是仍然会继续运行这个函数，直到return a,b为止。所以也算是一个递归。
ret = func(1,7)
print(ret)

# 第二个测试
def func(arg):
   arg.append(55)#没有返回内容，只是一个操作过程。
li = [11, 22, 33, 44]
func(li)
print(li)
li = func(li)
print(li)

#第三个测试
def func():
   name = "seven"
   def outer():
       name = "eric"
       def inner():
           global name
           name = "蒙逼了吧..."
       print(name)
   print(name)
ret = func()#打印的竟然是seven,因为outer()函数并没有被运行


name = "root"
def func():
   name = "seven"

   def outer():
       name = "eric"
       def inner():
           global name
           name = "蒙逼了吧..."
       print(name)
   o = outer()#这样，才会运行outer内部的代码
   print(o)
   print(name)

ret = func()
print(ret)
print(name)


name = "root"
def func():
   name = "seven"
   def outer():
       name = "eric"
       def inner():
               global name
               name = "..."
       print(name)
       inner()
   o = outer()
   print(o)
   print(name)

ret = func()
print(ret)
print(name)

name = "root"
def func():
    name = "seven"
    def outer():
        name = "eric"
        def inner():
            nonlocal name
            name = "蒙逼了吧..."
            print(name)
        inner()
    o = outer()
    print(o)
    print(name)

ret = func()
print(ret)
print(name)

#第四个测试
# n*(n-1)*....1

def f(n):
    if n==1:
        return 1
    return n*f(n-1)  #8*f(7)    7*f(6)  6*f(5).....  3*2    2*1
print(f(8))#这就是递归


#第五个测试
def func(x, y=0):
    y += 1#x=1,y=1
    if y == 5:
        return x + y
    x += y#x=2,y=1
    func(x, y)#并没有跳入这个函数中，直接执行了下面的代码返回x
    x += y
    return x
num = 1
result = func(num)
print(result)

