'''
第一个测试
类属性
下面我们定义了一个Chinese类。
这个对象类有一个属性country，是这个类所具有的，每个从这个类实例化的对象都有这个属性。
初始化init函数中定义了每个实例对象的name属性
还有具有一个play_ball的动作
python是没有真正的私有和公共的概念的
这个例子的重点在于如何从类外面修改类内部的动作属性
'''
class Chinese:
    country='China'
    def __init__(self,name):
        self.name=name
    def play_ball(self,ball):
        print('%s 正在打 %s' %(self.name))
#查看类属性，类属性不需要实例化就可以查看
print(Chinese.country)
#修改,因为目前这个类属性是公共的，所以可以直接修改
Chinese.country='Japan'
print(Chinese.country)
p1=Chinese('alex')
print(p1.__dict__)
print(p1.country)
#增加一个类属性
Chinese.dang='共产党'
# print(Chinese.dang)
# print(p1.dang)
#删除类属型
del Chinese.dang
del Chinese.country
print(Chinese.__dict__)
# print(Chinese.country)
def eat_food(self,food):
    print('%s 正在吃%s' %(self.name,food))
#这里演示了如何给一个类增加动作，
Chinese.eat=eat_food
print(Chinese.__dict__)
p1.eat('屎')
def ceshi(self):
    print('test')
##这里演示了修改类的某个动作，
Chinese.play_ball=ceshi
p1.play_ball()# Chinese.play_ball(p1)

'''
第二个例子
实例属性
实例只的是对类进行初始化得到的独特的一个对象。
实例的变量和方法也可以进行增改删的操作
'''
class Chinese:
    country='China'
    def __init__(self,name):
        self.name=name
    def play_ball(self,ball):
        print('%s 正在打 %s' %(self.name,ball))
p1=Chinese('alex')
print(p1.__dict__)
#查看
# print(p1.name)
# print(p1.play_ball)
#增加
p1.age=18
print(p1.__dict__)
print(p1.age)
#不要修改底层的属性字典
# p1.__dict__['sex']='male'
# print(p1.__dict__)
# print(p1.sex)
#修改
p1.age=19
print(p1.__dict__)
print(p1.age)
#删除
del p1.age
print(p1.__dict__)