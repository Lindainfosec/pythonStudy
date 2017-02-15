#!/usr/bin/env python
#-*-coding:utf-8-*-
fobj = open("sample.txt") #打开文件
'''
三种模式，默认只读：
"r"，以只读模式打开，你只能读取文件但不能编辑/删除文件的任何内容
"w"，以写入模式打开，如果文件存在将会删除里面的所有内容，然后打开这个文件进行写入
"a"，以追加模式代开，写入到文件中的任何数据将自动添加到末尾
'''

fobj
fobj.close() #关闭文件

fobj.read() #读取整个文件，需要先open才行
'''
read(size) 有一个可选的参数 size，用于指定字符串长度。
如果没有指定 size 或者指定为负数，就会读取并返回整个文件。当文件大小为当前机器内存两倍时，就会产生问题。
'''

fobj.readline() #读取每一行

fobj.readlines() #将每一行读取到一个列表中

for x in fobj:
    print(x, end = '')
    #循环遍历读取每一行

#接受用户输入的字符串作为将要读取的文件的文件名，并且在屏幕上打印文件内容。
#!/usr/bin/env python3
name = input("Enter the file name: ")
fobj = open(name)
print(fobj.read())
fobj.close()

fobj = open("aaa.txt", 'w') #写入模式
fobj.write('1111111111111')
fobj.write('222222\n')
fobj.write('3333\n')
fobj.write('end')
fobj.close()

fobj  = open('aaa.txt')
s = fobj.read()
fobj.close()
print(s)

#拷贝文件
#!/usr/bin/env python3
import sys
if len(sys.argv) < 3:
    print("Wrong parameter")
    print("./copyfile.py file1 file2")
    sys.exit(1)
f1 = open(sys.argv[1])
s = f1.read()
f1.close()
f2 = open(sys.argv[2], 'w')
f2.write(s)
f2.close()

#对任意给定文本文件中的制表符、行、空格进行计数。
#!/usr/bin/env python3
import os
import sys

def parse_file(path):
    """
    分析给定文本文件，返回其空格、制表符、行的相关信息

    :arg path: 要分析的文本文件的路径

    :return: 包含空格数、制表符数、行数的元组
    """
    fd = open(path)
    i = 0
    spaces = 0
    tabs = 0
    for i,line in enumerate(fd):
        spaces += line.count(' ')
        tabs += line.count('\t')
    # 现在关闭打开的文件
    fd.close()

    # 以元组形式返回结果
    return spaces, tabs, i + 1

def main(path):
    """
    函数用于打印文件分析结果

    :arg path: 要分析的文本文件的路径
    :return: 若文件存在则为 True，否则 False
    """
    if os.path.exists(path):
        spaces, tabs, lines = parse_file(path)
        print("Spaces {}. tabs {}. lines {}".format(spaces, tabs, lines))
        return True
    else:
        return False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)

#打开文件，自动关闭文件，就算发生异常也没关系。
with open('sample.txt') as fobj:
    for line in fobj:
         print(line, end = '')


# lscpu是对cat /proc/cpuinfo的输出美化



