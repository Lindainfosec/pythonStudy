#!/usr/bin/env python
#-*-coding:utf-8-*-
age = 21
counter = 0
for i in range(10):
    if counter < 3:
        guess_num = int(input("input age use number"))
        if guess_num == age:
            print("ok")
            break
            #可以在输入正确后，跳出循环。
        elif guess_num > age:
            print("年龄太大！")
        else:
            print("年龄太小！")
    else:
        #print("too many attempts ")
        #break
        continue_confirm = input("do you want to continue? yes or no")
        if continue_confirm =='yes':
            counter = 0
            # pass  一个占位符。到这里不执行，但又保证整体结构正确。
        else:
            print("bye")
            break

    counter=counter+1
# for i in range(10):
#     print(i)

#选中后，按tab键缩进，按shift加tab键可以反向缩进