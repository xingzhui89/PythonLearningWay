#第一个测试
movie_people = ['sb_alex', 'sb_wupeiqi', 'linhaifeng', 'sb_yuanhao']


def filter_test(array):
    ret = []
    for p in array:
        if not p.startswith('sb'):
            ret.append(p)
    return ret


res = filter_test(movie_people)
print(res)


#第二个测试
movie_people = ['alex_sb', 'wupeiqi_sb', 'linhaifeng', 'yuanhao_sb']
def sb_show(n):
    return n.endswith('sb')#返回的是bool变量
def filter_test(func, array):#传入函数做变量
    ret = []
    for p in array:
        if not func(p):
            ret.append(p)
    return ret
res = filter_test(sb_show, movie_people)
print(res)




#终极版本
movie_people=['alex_sb','wupeiqi_sb','linhaifeng','yuanhao_sb']
def sb_show(n):
    return n.endswith('sb')
#--->lambda n:n.endswith('sb')# 如果使用匿名函数，会更简洁
def filter_test(func,array):
    ret=[]
    for p in array:
        if not func(p):
               ret.append(p)
    return ret
res=filter_test(lambda n:n.endswith('sb'),movie_people)
print(res)

#filter函数
#通过一些函数来对序列中的元素进行筛选，最终获取符合条件的序列/。
movie_people=['alex_sb','wupeiqi_sb','linhaifeng','yuanhao_sb']
print(filter(lambda n:not n.endswith('sb'),movie_people))#打印一个filter对象

res=filter(lambda n:not n.endswith('sb'),movie_people)
print(list(res))#要转化成列表才能输出

print(list(filter(lambda n:not n.endswith('sb'),movie_people)))