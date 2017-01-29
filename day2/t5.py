#!/usr/bin/env python
#-*-coding:utf-8-*-
#元组（不可变列表）

name=(1,2,3,4,5,6,7,8,9,1212,12)
print (type (name))
#赋值以后不能修改。
#可以进行索引和查询。
# name.count(3)
# name.index(3)

username=input("please input username:")
if username.strip() == 'aaa':
#if username.strip('\n') == 'aaa':
    #strip（移除空白）可以避免用户输入了空格导致的读取错误。也可以在括号内指定忽略的输入内容。
    print("wellcome")
else:
    print("bye")

name1="aaa,qwe,asdasd,zxczxcz,qwe,asd,qwxs"
name2=name1.split(",")
print(name2) #输出一个分割的列表。
print("|".join(name2))  #按照|作为分隔符输出

name3="admin tom"
print(name3.capitalize()) #首字母大写进行输出

msg="hello {name4} ,can you tell me the {num} "
msg1=msg.format(name4='aaa',num=21)
msg2="Do you have {0},do you want to play the {1}"
print(msg1)
print(msg2.format('qwe','asd'))
print(name3.center(40,'-'))  #占用40个位置，让name3的值居中显示，其他空位用 - 填充起来
