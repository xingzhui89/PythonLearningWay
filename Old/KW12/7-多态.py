'''
多态的定义
由不同的类实例化得到的对象，调用同一个方法，执行的逻辑不同。
多态的概念指出了对象如何通过他们共同的属性和动作来操作及访问，而不需要考虑他们具体的类。

在python中一切皆对象，不同的对象可以调用相同的方法。
比如说del删除命令，可以作用于不同的变量，比如数字，字符，列表等。
再比如，len()方法，可以用来计算字符串，列表，元组的长度，所以这些对象都可以调用len方法。

在下面的实例中，我们定义了一个H2O类，这个类包含name和temperature属性，包含了turn_ice()方法。
然后我们通过继承的方法，定义了Water、Ice和Steam类。
这些子类中都没有具体的属性和方法实现。

在分别初始化这几个子类之后，我们使这几个实例都调用turn_ice方法，是可以运行的。
我们再来考虑一下，turn_ice函数中的self，表示的是H2O类，子类的实例之所以能够调用该函数，说明子类实例本质上还是H2O类的。
'''

class H2O:
    def __init__(self,name,temperature):
        self.name=name
        self.temperature=temperature
    def turn_ice(self):
        if self.temperature < 0:
            print('[%s]温度太低结冰了' %self.name)
        elif self.temperature > 0 and self.temperature < 100:
            print('[%s]液化成水' %self.name)
        elif self.temperature > 100:
            print('[%s]温度太高变成了水蒸气' %self.name)
    def aaaaaa(self):
        pass

class Water(H2O):
    pass
class Ice(H2O):
    pass
class Steam(H2O):
    pass

w1=Water('水',25)
i1=Ice('冰',-20)
s1=Steam('蒸汽',3000)

w1.turn_ice()
i1.turn_ice()
s1.turn_ice()

'''
我们再来考虑一下，如果不想通过每个实例来调用turn_ice()方法，可否定义一个函数，这个函数能够接收所有的子类实例，并且运行实例的方法。
请看下面的例子。

与上面的执行结果是完全相同的。
这是动态语言和静态语言（例如Java）最大的差别之一。动态语言调用实例方法，不检查类型，只要方法存在，参数正确，就可以调用。
'''
def func(obj):
    obj.turn_ice()
func(w1)
func(i1)
func(s1)
