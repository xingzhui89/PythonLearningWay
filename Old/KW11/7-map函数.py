num_l=[1,2,10,5,3,7]
num1_l=[1,2,10,5,3,7]

# ret=[]
# for i in num_l:
#     ret.append(i**2)
#将num_l中的所有元素做了一个平方的运算，然后添加到了ret列表中
# print(ret)

def map_test(array):
    ret=[]
    for i in array:
        ret.append(i**2)
    return ret
#设置一个函数
ret=map_test(num_l)
rett=map_test(num1_l)
print(ret)
print(rett)

num_l=[1,2,10,5,3,7]
#lambda x:x+1
def add_one(x):
    return x+1

#lambda x:x-1
def reduce_one(x):
    return x-1

#lambda x:x**2
def pf(x):
    return x**2

def map_test(func,array):
    ret=[]
    for i in array:
        res=func(i) #add_one(i)
        ret.append(res)
    return ret
# print(map_test(add_one,num_l))
# print(map_test(lambda x:x+1,num_l))

# print(map_test(reduce_one,num_l))
# print(map_test(lambda x:x-1,num_l))

# print(map_test(pf,num_l))
# print(map_test(lambda x:x**2,num_l))



#终极版本
def map_test(func,array): #func=lambda x:x+1    arrary=[1,2,10,5,3,7]
    ret=[]
    for i in array:
        res=func(i) #add_one(i)
        ret.append(res)
    return ret

print(map_test(lambda x:x+1,num_l))
res=map(lambda x:x+1,num_l)
print('内置函数map，处理结果',res)
# for i in res:
#     print(i)
print(list(res))
print('传的是有名函数',list(map(reduce_one,num_l)))


msg='linhaifeng'
print(list(map(lambda x:x.upper(),msg)))

#map函数就是通过传入的函数，对序列中的元素进行操作

