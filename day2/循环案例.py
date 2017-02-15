#!/usr/bin/env python
#-*-coding:utf-8-*-

# 斐波那契（Fibonacci）数列
a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b

a, b = 0, 1
while b < 100:
    print(b, end=' ')
    a, b = b, a + b
print()


#乘法表
i = 1
print("-" * 50)
while i < 11:
    n = 1
    while n <= 10:
        print("{:4d}".format(i * n), end=' ')
        n += 1
    print()
    i += 1
print("-" * 50)

#
# 's' * 10
# 'ssssssssss'
# print("*" * 10)
# **********
#  print("#" * 20)
# ####################
# print("--" * 20)
# ----------------------------------------
#  print("-" * 40)
# ----------------------------------------

#倒立直角三角形
row = int(input("Enter the number of rows: "))
n = row
while n >= 0:
    x =  "*" * n
    print(x)
    n -= 1

#正立直角三角形
n = int(input("Enter the number of rows: "))
i = 1
while i <= n:
    print("*" * i)
    i += 1

#倒立直角三角形的对称
row = int(input("Enter the number of rows: "))
n = row
while n >= 0:
    x = "*" * n
    y = " " * (row - n)
    print(y + x)
    n -= 1



