#某班上有n位同学，那么至少有两个人生日相同的概率？
for n in range(10,101,10):
    result = 1
    for i in range(1,n):
        result=result*(1-i/365)
    print('当n=:'+str(n)+'时，对应概率为：'+str(1-result))