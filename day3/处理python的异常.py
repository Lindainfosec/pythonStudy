#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
当有人试图访问一个未定义的变量则会发生 NameError。
在 Python3 中使用 Python2 独有的语法就会发生 SyntaxError
在行首多打了一个空格就会产生 IndentationError
当操作或函数应用于不适当类型的对象时引发TypeError

try except工作过程：
首先，执行 try 子句 （在 try 和 except 关键字之间的部分）。

如果没有异常发生，except 子句 在 try 语句执行完毕后就被忽略了。

如果在 try 子句执行过程中发生了异常，那么该子句其余的部分就会被忽略。

如果异常匹配于 except 关键字后面指定的异常类型，就执行对应的 except 子句。然后继续执行 try 语句之后的代码。

如果发生了一个异常，在 except 子句中没有与之匹配的分支，它就会传递到上一级 try 语句中。

如果最终仍找不到对应的处理语句，它就成为一个 未处理异常，终止程序运行，显示提示信息。

'''


def get_number():
    "Returns a float number"
    number = float(input("Enter a float number: "))
    return number

while True:
    try:
        print(get_number())
    except ValueError:
        print("You entered a wrong value.")


# 一个空的 except 语句能捕获任何异常。阅读下面的代码：
try:
    input() # 输入的时候按下 Ctrl + C 产生 KeyboardInterrupt
except:
    print("Unknown Exception")

#raise抛出异常
try:
    raise ValueError("A value error happened.")
except ValueError:
    print("ValueError in our code.")


try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
#不管有没有发生异常，finally 子句 在程序离开 try 后都一定会被执行。
# 当 try 语句中发生了未被 except 捕获的异常（或者它发生在 except 或 else 子句中），
# 在 finally 子句执行完后它会被重新抛出。
# 在真实场景的应用程序中，finally 子句用于释放外部资源（文件或网络连接之类的），无论它们的使用过程中是否出错。

