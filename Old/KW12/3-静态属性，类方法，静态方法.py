'''
静态属性和类方法，静态方法
下面这段代码我们定义了一个Room类，除了常规的属性和方法外，我们多了三个装饰器。
1、一个是property
这个装饰器的作用是将类的方法转换成一个类似于属性一样可以直接调用的，不需要加括号就可以。
好处是可以封装具体的实现形式
2、一个是classmethod
这个装饰器的作用是将类的方法转换成一个类方法，这样可以直接通过类来调用，不需要通过任何实例。
其中的cls表示当前类。类方法不需要传入self参数了。类方法只能通过类来执行，跟类绑定的，无法访问实例属性。
3、最后是staticmethod
这个是静态方法，该方法无法访问实例属性。但是实例可以调用这个方法。既不与类绑定，也不与具体实例绑定

这个类中的test方法，它需要传入实例作为参数才可以调用。
或者实例直接调用这个test方法。跟实例绑定的
'''
class Room:
    tag=1
    def __init__(self,name,owner,width,length,heigh):
        self.name=name
        self.owner=owner
        self.width=width
        self.length=length
        self.heigh=heigh
    @property
    def cal_area(self):
        return  self.width * self.length
    def test(self):
        print('from test',self.name)
    @classmethod
    def tell_info(cls,x):
        print(cls)
        print('--》',cls.tag,x)
    @staticmethod
    def wash_body(a,b,c):
        print('%s %s %s正在洗澡' %(a,b,c))

r=Room('厕所','alex',100,100,100000)
print(r.name)
print(r.cal_area)
r.test()
Room.tell_info(10)
Room.test(r)
r.tell_info(10)#函数没有执行
Room.wash_body('alex','yuanhao','wupeiqi')
r.wash_body('alex','yuanhao','wupeiqi')