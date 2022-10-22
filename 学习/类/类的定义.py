'''
数据封装：在类内部定义访问数据的方法，实现数据的‘封装’。
实现苏剧的封装后，在实例变量上调用时，不需要知道内部的实现细节。

 _xxx：这样的对象叫做保护成员，模块中这样的对象默认不能用from module import * 导入
__xxx__：系统定义的特殊成员。
__xxx：类中的私有成员，只有该类对象自己能访问。子类对象也不能访问这个成员，
 在对象外部可以通过“对象名._类名__xxx”这样的特殊方式访问
'''
class people:
    #初始化一个对象的各个属性
    def __init__(self, name, age=22, firstname='耶', gender='男'):  # 构造方法
        self.__name = name
        self.__firstname = firstname
        self.__gender = gender
        self.age = age
    #定义方法
    def info(self):
        print(f'我是一个{self.__gender}人，名字叫{self.__name},来自{self.__firstname}家族')
        # f'xxx {}  xxx'

    def Ican(self):
        if int(self.age) >= 23:
            print(f'我今年{self.age}岁，已经工作了')
        else:
            print(f'我今年{self.age}岁，我还在学习')

a = people("亚当",30)
# 继承是为代码复用和设计复用而设计的
#在继承关系中，已有的、设计好的类称为父类或基类，新设计的类称为子类或派生类。
#派生类可以继承父类的共有成员，但是不能继承其私有成员。
#如果需要在派生类中调用基类的方法，可以使用内置的super()或者通过”基类名.方法名()“的方法
class man(people):
    def gender(self):
        self.gender = '男'

class woman(people):
    def gender(self):
        self.gender = '女'

class child(people):
    pass

a = man('亚当',25)
b = woman('夏娃', 22)
c = child('盖伊', 5)

a.info()
a.Ican()
print("\n")
b.info()
b.Ican()
print("\n")
c.info()
c.Ican()