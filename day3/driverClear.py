#!/usr/bin/env python
#-*-coding:utf-8-*-

# 系统盘 %system% 下文件类型：
# 【临时文件（*.tmp）】
# 【临时文件（*._mp）】
# 【日志文件（*.log）】
# 【临时帮助文件（*.gid）】
# 【磁盘检查文件（*.chk）】
# 【临时备份文件（*.old）】
# 【Excel备份文件（*.xlk）】
# 【临时备份文件（*.bak）】
# --------------------------------
# 用户目录 %userprofile% 下文件夹
# 【COOKIE】 cookies\*.*
# 【文件使用记录】 recent\*.*
# 【IE临时文件】 Temporary Internet Files\*.*
# 【临时文件文件夹】 Temp\*.*
# --------------------------------
# Windows 目录 %windir% 下文件夹
# 【预读取数据文件夹】 prefetch\*.*
# 【临时文件】 temp\*.*

# 获取当前目录路径
import os
os.getcwd()

# 跳转至指定的文件目录
os.chdir('d://temporary')
os.getcwd()

# 获取系统盘符
os.environ['systemdrive']

# 获取用户目录
os.environ['userprofile']

# 获取 Windows 目录
os.environ['windir']

# 删除文件
os.remove('d:temporary/test/test.txt')

# 删除文件夹,os.rmdir 只能删除空文件夹，如果文件夹非空，则会报错。
os.rmdir('d:temporary/test/empty')

# 引用另外一个模块 shutil 的函数来删除非空文件夹
import shutil
shutil.rmtree('d:/temporary/test/aaa')
# os.system('rd/s/q "d:temporary/test"')

