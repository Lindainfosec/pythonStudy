#!/usr/bin/env python
#-*-coding:utf-8-*-

#判断一个列表中的数值的数量。
age=12
name=['aaa',"jack","rain",9,3,5,67,2,45,73,643,12,4,'qasd','axcq','moni',12,4557,1195,325,6,9,34,6,age]
name2=['aaa',"jack","rain",[1,2,3,4,5],9,3,5,67,2,45,73,643,12,4]
name[4][1]=2222222
#修改数值  import copy  调用copy库。 ctrl+左键点击一些内容，可以查看更多。
#print("name2",len(name2)) 查看name2的长度。
name.append(112)
#在name列表最后添加一个112
name.count(111)
#输出111在name列表中出现的次数

name.remove(111)
#在name中删除111

name.reverse()
#反转输出列表

del name[-1]
#删除列表最后一个元素

name.extend(111)
#在列表最后追加111

name.sort()
#对列表进行排序

# 栈是我们通常所说的一种 LIFO （Last In First Out 后进先出）数据结构。
name.pop()
#从最后一个开始，一个一个的取出元素，一次取一个，直到列表被取空为止。

squares = [x**2 for x in range(10)]
#快速创建一个列表squares

z=[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
z1 = [x + 1 for x in [x ** 2 for x in z]]
#创建两个列表的元素，然后做嵌套

# name3=name.copy()
#name4=copy.deepcopy()  深copy
# print(name3)
#复制一个列表。然后打印出来。

# name.extend(name2)
# print(name)
#把name2追加到name，然后输出name列表，extend换为reverse可以反转。

if 9 in name:
    num_of_name=name.count(9)
    print("[%s] 9 is in name" %num_of_name)
# if 9 in name:
#     print("9 is in name")
#    判断这个列表中存在9这个数值。


