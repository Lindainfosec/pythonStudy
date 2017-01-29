#!/usr/bin/env python
#-*-coding:utf-8-*-

#print( '\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))  #输出九九乘法表

#print('\n'.join([''.join([('AndyLove'[(x - y) % 8] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else' ')for x in range(-30, 30)]) for y in range(15, -15, -1)]))
#输出一个心状图案

#print(*(i for i in range(2, 1000) if all(tuple(i%j for j in range(2, int(i**.5))))))
#输出1-1000之间的素数

