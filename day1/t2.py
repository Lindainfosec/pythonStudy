#!/usr/bin/env python
#-*-coding:utf-8-*-

name=input("input your name:")
age=input("input your age:")
#age=int(input("input your age:")) 可以通过int，强制把输入的转换成数字，因为在py3中，input默认输入的是字符
job=input("input your job:")
#将光标移动到行末，按住ctrl+D，自动复制这一行
#进行一个输入操作
#选中多行，然后按ctrl+/ ，即可注释多行
#选中内容以后，按table键可以让选中的内容自动被table，按shift+table可以还原到上一个被table的状态。
print("name is:",name)
print("age is:",age)
print("job is:",job)
#将输入的内容输出
msg='''
Infomation of user %s:
---------------------
name: %s
age : %s
job : %s
---------------------
'''%(name,name,age,job)
print(msg)