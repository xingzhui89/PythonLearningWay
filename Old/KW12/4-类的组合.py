'''
类的组合
如果我们定义的两个对象之间具有很强的相关性，那么我们可以将两个类组合起来，实现比较复杂的表达。
比如一个学校类，具有name和addr两个属性；一个课程类，具有name，price，period和school四个属性。
其中课程类的school属性，就完全可以用一个学校类的实例对象来表示，而不用单独再定义一个名称或者一个字典来表示school的内容。
我们看代码来分析：
'''

class School:
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
    def zhao_sheng(self):
        print('%s 正在招生' %self.name)

class Course:
    def __init__(self,name,price,period,school):
        self.name=name
        self.price=price
        self.period=period
        self.school=school

s1=School('oldboy','北京')
s1.zhao_sheng()
s2=School('oldboy','南京')
s3=School('oldboy','东京')

msg='''
1 老男孩 北京校区
2 老男孩 南京校区
3 老男孩 东京校区
'''
while True:
    print(msg)
    menu={
        '1':s1,
        '2':s2,
        '3':s3
    }
    choice=input('选择学校>>: ')
    school_obj=menu[choice]
    name=input('课程名>>： ')
    price=input('课程费用>>： ')
    period=input('课程周期>>： ')
    new_course=Course(name,price,period,school_obj)
    print('课程【%s】属于【%s】学校' %(new_course.name,new_course.school.name))