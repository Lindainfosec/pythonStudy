#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

'''
a=['ales','aaa','tom']
for index.i in enumerate(a):
    print(index.i)
打印时不仅输出数组的内容，还会在前面加上顺序的数字标号。输出是括号括起来的。
isdigit()方法用于检测字符串是否全是数字组成的。

'''

salary = input("Input your salary:") #输入工资，并且判断是不是数字。如果不是就退出。
if salary.isdigit():
    salary = int(salary)
else:
    exit("Invaild data type...")

welcome_msg = 'Welcome to Alex Shopping mall'.center(50,'-')
print(welcome_msg)#打印欢迎信息

exit_flag = False
product_list = [
    ('Iphone',5888),
    ('Mac Air',8000),
    ('Mac Pro',9000),
    ('XiaoMi 2',19.9),
    ('Coffee',30),
    ('Tesla',820000),
    ('Bike',700),
    ('Cloth',200),]
#打印商品价格列表，价格因为会出现修改，需要写成字典。如果一次就写死了，以后修改不方便。字典默认是无序的。

shop_car = []
while  exit_flag is not True:
    #for product_item in product_list:
    #    p_name,p_price = product_item
    #for p_name,p_price in product_list:
    print("product list".center(50,'-'))
    for item in enumerate(product_list):
        index = item[0]
        p_name = item[1][0]
        p_price = item[1][1]
        print(index,'.',p_name,p_price)

    user_choice = input("[q=quit,c=check]What do you want to buy?:")
    if user_choice.isdigit():#肯定是选择shangpin
        user_choice = int(user_choice)
        if user_choice < len(product_list):
            p_item = product_list[user_choice]
            if p_item[1] <= salary: #买的起
                shop_car.append(p_item) #放入购物车
                salary -= p_item[1] #减钱
                print("Added [%s] into shop car,you current balance is \033[31;1m[%s]\033[0m" %
                      (p_item,salary))
            else:
                print("Your balance is [%s],cannot afford this.." % salary)
    else:
        if user_choice == 'q' or user_choice =='quit':
            print("purchased products as below".center(40,'*'))
            for item in shop_car:
                print(item)
            print("END".center(40,'*'))
            print("Your balance is [%s]" % salary)
            print("Bye")
            exit_flag = True
        elif  user_choice == 'c' or user_choice =='check':
            print("purchased products as below".center(40,'*'))
            for item in shop_car:
                print(item)
            print("END".center(40,'*'))
            print("Your balance is \033[41;1m[%s]\033[0m" % salary)

