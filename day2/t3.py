#!/usr/bin/env python
#-*-coding:utf-8-*-
age=11
name=["aaa","qqq","zzz",21,age,"qwe","asd","zxc"]
#python中叫做列表，其他语言中叫做数组。可以存储变量，数字，字符。列表下标是从0开始计数的。

print(name[1])
print(name)
print(name[-2])

print(name[0:2])
print(name[:3])
print(name[-0])
print(name[-1:-5])
print(name[:7][2:4][0][1])
#切片。取头不取尾,可以不断的切分。

name[1]="qaz"
#对列表中第二个值进行更新修改。
name.insert(2,'wsx')
#在列表第三个位置，插入一个值。

name.append("edc")
#在列表后面追加一个值。

name.remove("wsx")
#直接在列表删除一个值

name2=name[2:5]
print(name2)

name.insert(1,'qweqwe')
name.insert(2,'asdasd')
del name[1:3]
#python中del，可以删除python任何存储的数据。del name 可以删除整个列表。

print(name[0:-1:2])
# print(name[0::2])
# print(name[::2])
#输出列表，除了最后一个值，每隔一个值输出一次值。最后一个值是步长。以上方法均可。默认步长是1



