#!/usr/bin/env python
#-*-coding:utf-8-*-


#在类的声明中你可以写任何 Python 语句，包括定义函数（在类中我们称为方法）。
class MyClass(object):
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

x = MyClass()
# 以上创建了一个新的类实例并将该对象赋给局部变量 x。

'''
很多类都倾向于将对象创建为有初始状态的。因此类可能会定义一个名为 __init__() 的特殊方法，像下面这样:

def __init__(self):
    self.data = []

出于弹性的需要，__init__() 方法可以有参数。事实上，参数通过__init__() 传递到类的实例化操作上。例如：
class Complex:
    def __init__(self, realpart, imagpart):
         self.r = realpart
         self.i = imagpart
x = Complex(3.0, -4.5)
x.r, x.i


>>> class Student(object):
...     def __init__(self, name):
...         self.name = name
...
>>> std = Student("Kushal Das")
>>> print(std.name)
Kushal Das
>>> std.name = "Python"
>>> print(std.name)
Python



'''

#!/usr/bin/env python3
class Person(object):
    """
    返回具有给定名称的 Person 对象
    """
    def __init__(self, name):
        self.name = name

    def get_details(self):
        "返回包含人名的字符串"
        return self.name

class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """
    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        "返回包含学生具体信息的字符串"
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

person1 = Person('Sachin')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())


s = "I love you"
del s
#删除一个对象


#装饰器

#!/usr/bin/env python3

class Account(object):
    """账号类,
    amount 是美元金额.
    """
    def __init__(self, rate):
        self.__amt = 0
        self.rate = rate

    @property
    def amount(self):
        "账号余额（美元）"
        return self.__amt

    @property
    def cny(self):
        "账号余额（人名币）"
        return self.__amt * self.rate

    @amount.setter
    def amount(self, value):
        if value < 0:
            print("Sorry, no negative amount in the account.")
            return
        self.__amt = value

if __name__ == '__main__':
    acc = Account(rate=6.6) # 基于课程编写时的汇率
    acc.amount = 20
    print("Dollar amount:", acc.amount)
    print("In CNY:", acc.cny)
    acc.amount = -100
    print("Dollar amount:", acc.amount)
