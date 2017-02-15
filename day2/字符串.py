#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

#names = "alex,jack,rain"

#name2= names.split(",")
#print(name2)
#print( "|".join(name2) )
#username = input("user:")
#if username.strip() == 'alex':
#    print("welcome")

name = "alex li"
#print(name[2:4])
#print(name.center(40,'-') )
#print(name.find('sdfs') )

#print('' in name) #有没有空格

#print(name.capitalize())
#msg = "Hello, {name}, it's been a long {age} since last time sopke..."
#msg2 = "hahah{0}, dddd{1}"
#print(msg2.format('Alex',33))
#msg2 = msg.format(name='MingHu', age=333)
#print(msg2)
'''
age = input("your age:")
if age.isdigit():
    age = int(age)
else:
    print("invalid data type")
    '''
name ='alex3sdf'
print(name.isalnum() )
print(name.endswith('dfsd') )
print(name.startswith('dfsd') )
print(name.upper().lower())


s = "shi yan lou "
s.title()
#每个单词的首字母大写输出

z = s.upper()
print(z) #输出全都大写

z.lower() #输出全都小写

s = "I am A pRoGraMMer"
s.swapcase() #大小写互换
s.isalnum() #检查是否为数字和字母，带空格会返回false
s.isalpha() #检查是否都是字母，带空格会返回false
s.isdigit() #检查是否都是数字
s.islower() #检查是否都是小写
s.istitle() #检查是否是标题样式
s.isupper() #检查是否都是大写

s = "We all love Python"
s.split() #分割输出字符串

x = "shiyanlou:is:waiting"
x.split(':')  #以：分割字符串

"-".join("GNU/Linux is great".split())  #指定-来分割字符串
# 方法 join() 使用指定字符连接多个字符串，它需要一个包含字符串元素的列表作为输入然后连接列表内的字符串元素。

s = "  a bc\n "
s.strip() #用来剥离字符串首尾中指定的字符，它允许有一个字符串参数，这个参数为剥离哪些字符提供依据。不指定参数则默认剥离掉首尾的空格和换行符

s = "www.foss.in"
s.lstrip("cwsd.") #剥离左侧的内容

s.rstrip("cnwdi.") #剥离右侧的内容

s = "faulty for a reason"
s.find("for")
s.find("fora")
# find() 能帮助你找到第一个匹配的子字符串，没有找到则返回 -1

s.startswith("fa") # 检查字符串是否以 fa 开头

s.endswith("reason") # 检查字符串是否以 reason 结尾

# 回文是一种无论从左还是从右读都一样的字符序列。
#!/usr/bin/env python3
s = input("Please enter a string: ")
z = s[::-1]
if s == z:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

#单词计数
#!/usr/bin/env python3
s = input("Enter a line: ")
print("The number of words in the line are %d" % (len(s.split(" "))))


