#!/usr./bin/env python
# -*- coding:utf-8 -*-
#studySourceURL:https://www.bilibili.com/video/av12721444/
#python2 version
#通过（https://www.baidu.com/s?wd=useragent%E5%A4%A7%E5%85%A8&rsv_spt=1&rsv_iqid=0xf589e75b00007cae&issp=1&f=3&rsv_bp=0&rsv_idx=2&ie=utf-8&rqlang=&tn=baiduhome_pg&ch=&rsv_enter=1&inputT=4696）
#获取更多的user-agent

import random
#引入随机参数

headerstr = '''
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50
Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)
Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
'''
#可以添加多个user-agent信息

def headers():
    header = headerstr.split('\n')
    length = len(header)
    #用换行符，对headerstr里面的内容，切片。
    return header[random.randint(1,length-1)]
    #随机切片1到数据总长度的切片数量，元素是0开始的，所以要length-1