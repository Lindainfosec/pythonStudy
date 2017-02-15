#!/usr/bin/env python
#-*-coding:utf-8-*-

#!/usr/bin/env python3
def palindrome(s):
    return s == s[::-1]
if __name__ == '__main__':
    s = input("Enter a string: ")
    if palindrome(s):
        print("Yay a palindrome")
    else:
        print("Oh no, not a palindrome")

#局部变量
#!/usr/bin/env python3
def change():
    a = 90
    print(a)
a = 9
print("Before the function call ", a)
print("inside change function", end=' ')
change()
print("After the function call ", a)

#全局变量
#!/usr/bin/env python3
def change():
    global a
    a = 90
    print(a)
a = 9
print("Before the function call ", a)
print("inside change function", end=' ')
change()
print("After the function call ", a)


def test(a , b=10):
    if a>b:
        return True
    else:
        return False

test(1)
test(9,1)
#具有默认值的参数后面不能再有普通参数，比如 f(a,b=90,c) 就是错误的。


def f(a, data=[]):
    data.append(a)
    return data
#函数的累积输出
print(f(1))
print(f(2))
print(f(3))

def f(a, data=None):
    if data is  None:
        data=[]
        data.append(a)
    else:
        return data
#不累积的输出
print(f(1))
print(f(2))
print(f(3))

def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
#指定赋值某个参数
func(12, 24)
func(12, c = 24)
func(b=12, c = 24, a = -1)

#强制关键字参数
def hello(*, name='User'):
    print("hello",name)
hello('shiyanlou')
hello(name='shiyanlou')
#必须严格按照格式才能正常输出

#文档字符串
#!/usr/bin/env python3
import math

def longest_side(a, b):
    """
    Function to find the length of the longest side of a right triangle.

    :arg a: Side a of the triangle
    :arg b: Side b of the triangle

    :return: Length of the longest side c as float
    """
    return math.sqrt(a*a + b*b)

if __name__ == '__main__':
    print(longest_side.__doc__)
    print(longest_side(4,5))

#高阶函数
def high(func, value):
    return func(value)
lst = high(dir, int)
print(lst[-3:])


#map函数，它接受一个函数和一个序列（迭代器）作为输入，然后对序列（迭代器）的每一个值应用这个函数，返回一个序列（迭代器），其包含应用函数后的结果
lst = [1, 2, 3, 4, 5]
def square(num):
    return num * num
print(list(map(square, lst)))

#发邮件的案例
def sendmail():
    import smtplib
    from email.mime.text import  MIMEText
    from email.utils import formataddr

    msg =  MIMEText('邮件内容','plain','utf-8')
    msg['From'] = formataddr(["发件人",'woxiangchimianbao@126.com'])
    msg['TO'] = formataddr(["收件人",'shoujianren@domain.com'])
    msg['Subject'] = "主题"

    server = smtplib.SMTP("smtp.126.com",25)
    server.login("woxiangchimianbao@126.com","qwe123456")
    server.sendmail('woxiangchimianbao@126.com',['目标邮箱'],msg.as_string())
    server.quit()

sendmail()







