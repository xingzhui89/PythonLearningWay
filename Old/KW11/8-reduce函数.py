# from functools import reduce

# num_l=[1,2,3,100]

# res=0
# for num in num_l:
#     res+=num
#对num_l中的元素进行累加
# print(res)

# num_l=[1,2,3,100]
# def reduce_test(array):
#     res=0
#     for num in array:
#         res+=num
#     return res
#
# print(reduce_test(num_l))


# num_l=[1,2,3,100]

# def multi(x,y):
#     return x*y
#返回出入两个参数的乘积
##匿名函数，lambda x,y:x*y

# def reduce_test(func,array):
#     res=array.pop(0)#获取第一个元素，并从序列中移除
#     for num in array:
#         res=func(res,num)
#     return res
#
# print(reduce_test(lambda x,y:x*y,num_l))

num_l=[1,2,3,100]
def reduce_test(func,array,init=None):
    if init is None:
        res=array.pop(0)#如果没有参数的话，默认移除最后一个元素，
    else:
        res=init
    for num in array:
        res=func(res,num)#通过循环来实现累乘
    return res

print(reduce_test(lambda x,y:x*y,num_l,100))


#reduce函数
#reduce函数就是通过传入的函数，对序列内所有的元素进行累计操作
# from functools import reduce
# num_l=[1,2,3,100]
# print(reduce(lambda x,y:x+y,num_l,1))#最后一个参数
# print(reduce(lambda x,y:x+y,num_l))
#
