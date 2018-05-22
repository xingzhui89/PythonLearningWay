user_list=[
    {'name':'alex','passwd':'123'},
    {'name':'linhaifeng','passwd':'123'},
    {'name':'wupeiqi','passwd':'123'},
    {'name':'yuanhao','passwd':'123'},
]#自建用户列表,也可以从数据库中读取
current_dic={'username':None,'login':False}#记录当前状态,如果是全局变量，那么一旦验证通过，就会一直有效，这个变量应该设置在验证函数中？？？

#验证函数,装饰器
def auth_func(func):
    def wrapper(*args,**kwargs):
        if current_dic['username'] and current_dic['login']:#如果username不是none并且login为true,也就是说已经有用户登陆
            res = func(*args, **kwargs)#那么就运行func函数,
            return res#返回结果
        go=True
        while go:#我们添加了一个判断变量，用于判断是否已经登陆
            username=input('用户名：').strip()
            passwd=input('密码：').strip()
            for user_dic in user_list:
                if username == user_dic['name'] and passwd == user_dic['passwd']:#通过username和passwd验证
                    current_dic['username']=username
                    current_dic['login']=True#设置为当前用户
                    go=False
                    res = func(*args, **kwargs)
                    return res
            else:
                print('用户名或者密码错误')#这里有个问题，无法登陆的话，应该是退出程序或者重新出入用户名密码，怎么设计呢？

    return wrapper

@auth_func
def index():#设置登陆
    print('欢迎来到京东主页')

@auth_func
def home(name):#带参数
    print('欢迎回家%s' %name)

@auth_func
def shopping_car(name):
    print('%s的购物车里有［%s,%s,%s］' %(name,'奶茶','妹妹','娃娃'))

print('before-->',current_dic)
index()
print('after--->',current_dic)
home('产品经理')
shopping_car('产品经理')
