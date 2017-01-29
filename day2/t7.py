#!/usr/bin/env python
#-*-coding:utf-8-*-

count=0
while True:
    count += 1
    if count > 50 and count < 60:
        continue#当他是50到60之间的时候，直接跳过输出。
    print("hello python",count)

    if count==100:
        print("bye")
        break
#while循环语句。

