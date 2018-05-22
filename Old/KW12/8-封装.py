'''
封装
“封装”就是将抽象得到的数据和行为（或功能）相结合，形成一个有机的整体（即类）；
封装的目的是增强安全性和简化编程，使用者不必了解具体的实现细节，而只是要通过外部接口，一特定的访问权限来使用类的成员。

如何在类中实现封？就是是数据不能被外界访问，只能通过类中的方法。
可以通过将数据私有化的方法，在初始化的时候在属性前面加上__符合，是两个下划线。

在类内部，可以通过.__属性的方法来访问该属性，在类外面，即便实例化了，该实例也无法直接访问该属性。
我们将不希望被外界直到的属性，以及给外界访问数据的接口都包含在一个类中，就简单的实现了封装的含义。

'''

class Room:
    def __init__(self,name,owner,width,length,high):
        self.name=name
        self.owner=owner
        self.__width=width
        self.__length=length
        self.__high=high
    def tell_area(self):
        return self.__width * self.__length *self.__high
    def tell_width(self):
        return self.__width

r1=Room('卫生间','alex',100,100,10000)

#arear=r1.__width * r1.__length #这句代码会报错的
print(r1.tell_area())