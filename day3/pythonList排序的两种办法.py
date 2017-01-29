#!/usr/bin/env python
#-*-coding:utf-8-*-

# 方法1. 用 list 的内建函数 list.sort 进行排序
# list.sort(func=None, key=None, reverse=False)
L = [2,5,8,9,3]
print(L)

L.sort() #进行排序
print(L)

# 方法2. 用序列类型函数 sorted(list) 进行排序
# （从 python 2.4 开始）
L1 = [2,5,8,9,3,1]
print(L1)
sorted(L1)
print(sorted(L1))
# 两种方法的区别：
# sorted(list) 返回一个对象，可以用作表达式。原来的 list 不变，生成一个新的排好序的 list 对象。
# list.sort() 没有返回值，直接改变原有的 list。

L2 = [2,3,1,4]
L2.sort(reverse=True)#逆序排列
print(L2)

# 对第二个关键字排序
L3 = [('b',6),('a',1),('c',3),('d',4)]
L3.sort(key=lambda x:x[1])
print(L3)

# 用第二个关键字排过序后再用第一个关键字进行排序
L4 = [('d',2),('a',4),('b',3),('c',2)]
L4.sort(key=lambda x:(x[1],x[0]))
print(L4)
