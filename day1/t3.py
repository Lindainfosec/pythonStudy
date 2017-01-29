#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
import getpass

name=input("name:")
# 将用户输入的内容赋值给 name 变量
pwd = getpass.getpass("password：")

# 打印输入的内容
print(name,pwd)
'''

#调用系统命令
import os
os.system('df')
os.mkdir('dname')
cmd_res = os.popen("df -hT").read()
#将输出结果读取到cmd_res上。
print(cmd_res)

import sys
print(sys.path)
#直接返回一个模块的路径列表

