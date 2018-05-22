'''
继承可以实现代码重用，但是会使得父类和子类耦合在一起，实际使用意义不大。
我们常用继承来实现接口继承，声明某个子类兼容于某基类。
定义一个接口类，子类继承接口类，并实现接口中定义的方法。

在接口类中定义的方法，在子类中一定要实现才可以，但是父类中不需要实现。

为了保证在子类中一定实现接口类中的所有方法，我们在接口类中给方法加上一个装饰器，定义为虚方法。
具体实现方法请看下面的代码。
这样的话，如果在子类中有方法没有实现，那么就无法实例化。
'''
import abc
class All_file(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self):
        pass
    @abc.abstractmethod
    def write(self):
        pass

class Disk(All_file):
    def read(self):
        print('disk read')
    def write(self):
        print('disk write')
class Cdrom(All_file):
    def read(self):
        print('cdrom read')
    def write(self):
        print('cdrom write')
class Mem(All_file):
    def read(self):
        print('mem read')
    def write(self):
        print('mem write')

m1=Mem()
m1.read()
m1.write()

'''
在子类中调用父类的方法

'''
class Vehicle:
    Country='China'
    def __init__(self,name,speed,load,power):
        self.name=name
        self.speed=speed
        self.load=load
        self.power=power
    def run(self):
        print('开动啦')
        print('开动啦')
class Subway(Vehicle):
        def __init__(self,name,speed,load,power,line):
           Vehicle.__init__(self,name,speed,load,power)
           #super(Subway, self).__init__(name, speed, load, power)
           self.line=line
        def show_info(self):
            print(self.name,self.speed,self.load,self.power,self.line)
        def run(self):
            Vehicle.run(self)
            #super().run()
            print('%s %s 线，开动啦' %(self.name,self.line))
line13=Subway('北京地铁','10km/s',1000000000,'电',13)
line13.show_info()
line13.run()