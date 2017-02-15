#!/usr/bin/env python
#-*-coding:utf-8-*-
a = 'Fedora', 'ShiYanLou', 'Kubuntu', 'Pardus'
#元组不可编辑

# 要创建只含有一个元素的元组，在值后面跟一个逗号。

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
#集合自动去重

#一些集合的操作
a1 = set('abracadabra')
b = set('alacazam')
print(a1-b)#输出a有b没有的
print(a1|b) #输出存在a或者存在b的
print(a1&b) #输出同时存在a和b的
print(a1^b) #输出存在于a和b，但又不同时存在的
a1.pop()
a1.add('111') #从左侧添加


data = {'kushal':'Fedora', 'kart_':'Debian', 'Jace':'Mac'}
data['parthan'] = 'Ubuntu'
del data['kushal']
# 字典中的键必须是不可变类型，比如你不能使用列表作为键。

dict((('Indian','Delhi'),('Bangladesh','Dhaka')))
# dict() 可以从包含键值对的元组中创建字典。
for x, y in data.items():
    print("{} uses {}".format(x, y))
    #对字典进行遍历

data.setdefault('names', []).append('Ruby')
#给字典中数据添加元素

# for i, j in enumerate(['a', 'b', 'c']):
#     print(i, j)
#遍历

#  a = ['Pradeepto', 'Kushal']
#  b = ['OpenSUSE', 'Fedora']
#  for x, y in zip(a, b):
#     print("{} uses {}".format(x, y))
#同时对两个序列遍历


'''
判断学生成绩是否达标的程序，要求输入学生数量，以及各个学生物理、数学、历史三科的成绩，
如果总成绩小于 120，程序打印 “failed”，否则打印 “passed”。
'''
#!/usr/bin/env python3
n = int(input("Enter the number of students: "))
data = {} # 用来存储数据的字典变量
Subjects = ('Physics', 'Maths', 'History') # 所有科目
for i in range(0, n):
    name = input('Enter the name of the student {}: '.format(i + 1)) # 获得学生名称
    marks = []
    for x in Subjects:
        marks.append(int(input('Enter marks of {}: '.format(x)))) # 获得每一科的分数
    data[name] = marks
for x, y in data.items():
    total =  sum(y)
    print("{}'s total marks {}".format(x, total))
    if total < 120:
        print(x, "failed :(")
    else:
        print(x, "passed :)")


'''
计算两个矩阵的乘积。要求输入矩阵的行/列数（在这里假设我们使用的是 n × n 的矩阵）。
'''
#!/usr/bin/env python3
n = int(input("Enter the value of n: "))
print("Enter values for the Matrix A")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
print("Enter values for the Matrix B")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append([a[i][j] * b[j][i] for j in range(n)])
print("After matrix multiplication")
print("-" * 7 * n)
for x in c:
    for y in x:
        print(str(y).rjust(5), end=' ')
    print()
print("-" * 7 * n)