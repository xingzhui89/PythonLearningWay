'''
第一个测试：
在定义一个对象的时候，这个对象肯定具有一些属性，还有一些动作。
属性我们可以用变量或者常量来表示，动作就需要用到函数来表示
但是我们不可能为每一个对象重复的写相通的属性和动作，所以就需要采用面向对象的编程方式。
一种对象，我们把它的共有属性和动作定义在一起。
比如下面这个例子，我们定义了狗的概念。
其中jiao和chi_shi是狗的动作，name，gender，type等是狗的属性。
init函数是我们用来初始化一条狗，这样会好看一些。
我们把狗的动作jiao和chi_shi也定义在初始化函数中了，当然只是函数名，在使用函数的时候，还需要在后面加个括号才可以。
jiao和chi_shi两个函数需要传入参数，所以在调用时，要将对象本身传进去。
'''
def dog(name,gender,type):
    def jiao(dog):
        print('一条狗[%s]，汪汪汪' % dog['name'])
    def chi_shi(dog):
        print('一条[%s] 正在吃屎' % dog['type'])
    def init(name,gender,type):
        dog1 = {
            'name':name,
            'gender': gender,
            'type': type,
            'jiao':jiao,
            'chi_shi':chi_shi,
        }
        return dog1
    return init(name,gender,type)

d1=dog('元昊','母','中华田园犬')
d2=dog('alex','母','藏敖')
print(d1)
print(d2)
d1['jiao'](d1)
d2['chi_shi'](d2)

'''
第二个测试
我们来做个练习，来定义一个学校的对象。
还是使用一个函数将学校的所有动作和初始化包含进来。
请注意一下，这些函数相当于是内部函数，这些内部函数所需要的变量，有的是从外层函数传入，有的是自己定义的一个对象。
我们在初始化函数中，定义的是一个字典，包含了对象所有的属性和动作名，动作名就是函数名。
'''
def school(name, addr, type):
    def init(name, addr, type):
        sch = {
            'name': name,
            'addr': addr,
            'type': type,
            'kao_shi': kao_shi,
            'zhao_sheng': zhao_sheng,
        }
        return sch
    def kao_shi(school):
        print('%s 学校正在考试' % school['name'])
    def zhao_sheng(school):
        print('%s %s 正在招生' % (school['type'], school['name']))
    return init(name, addr, type)
s1 = school('oldboy', '沙河', '私立学校')
print(s1)
print(s1['name'])
s1['zhao_sheng'](s1)
s2 = school('清华', '北京', '公立学校')
print(s2)
print(s2['name'], s2['addr'], s2['type'])
s2['zhao_sheng'](s2)

'''
第三个测试
使用函数来定义对象毕竟不方便，我们用面向对象编程特有的语法class来实现面向对象设计
请看下面这个关于狗的对象设计
想比如使用函数来设计，不同点有：
1、使用class定义，不需要在外层传入参数
2、初始化函数使用__init__替换了，属性的定义不在使用字典的形式
3、每个内部函数的第一个参数都是self，也就是该类或者该对象本身
4、在内部函数中很方便的调用对象本身的属性
最后我们使用__dict__函数输出实例对象dog1的属性。
'''
class Dog:
    def __init__(self,name,gender,type):
        self.name=name
        self.gender=gender
        self.type=type
    def bark(self):
        print('一条名字为[%s]的[%s],狂吠不止' %(self.name,self.type))
    def yao_ren(self):
        print('[%s]正在咬人' %(self.name))
    def chi_shi(self):
        print('[%s]正在吃屎' %(self.type))
dog1=Dog('alex','female','京巴')
print(dog1.__dict__)
