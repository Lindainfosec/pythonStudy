#!/usr./bin/env python
# -*- coding:utf-8 -*-
#studySourceURL:https://www.bilibili.com/video/av12721444/
#python2 version
#看到了
#目标：https://mm.taobao.com

'''
分析页面数据
1、查看网站页面源代码
2、查看是否是ajax异步加载
在浏览器，按F12，查看network选项，刷新一下网页，看数据抓包，选择XHR选项，如果看到有值，点击查看，
查看preview，如果乱码，就在新的界面打开查看，或者换旧版本的浏览器尝试。
在headers里面获取到url
https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8
3、解密（熟悉前端，尤其是JavaScrip）
在headers中，Request Method是请求方式的描述。

反爬虫：判断浏览器的信息。根据user-agent判断访问者是否是bot
手动添加头部信息即可
'''

import urllib2
from coms import headers
#从coms文件中引入headers函数的值
from json import loads
#将标准字符串转换为dict
import re  #添加正则表达式的支持



def geturlList():
    req = urllib2.Request (
        'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8'
    ) #实例化一个请求的对象
    req.add_header('user-agent',headers())
    #手动添加头部信息
#print headers()  测试一下是否能正常取出headers里面的值
    html = urllib2.urlopen(req,data='q&viewFlag=A&sortType=default&searchStyle=&searchRegion=city%3A&searchFansNum=&currentPage=1&pageSize=100').read().decode('gbk').encode('utf-8')
    #data的值，还是在headers选项，在form data选项中，选择view source查看
    '''
    decode('') 解码，把一种编码，转换成unicode编码
    encode('') 编码，把unicode编码转换成其他编码
    .decode('gbk').encode('utf-8') 将数据从gbk转码成utf-8
    '''
    #print html #返回数据测试
    json = loads(html)
    return json['data']['searchDOList']
    #在preview选项中查看到data和searchDOList

def getInfo(userID):   #或许userID
    req = urllib2.Request('https://mm.taobao.com/self/aiShow.htm?userId=%s'%userID)
    req.add_header('user-agent',headers())
    html = urllib2.urlopen(req).read().decode('gbk').encode('utf-8')
    print html  #输出测试

def getAlbumList(userID):   #获取相册
    req = urllib2.Request('https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%%20=%s' %userID)  #出现多个%的时候，需要在%前面加一个%做转义
    req.add_header('user-agent', headers())
    html = urllib2.urlopen(req).read().decode('gbk').encode('utf-8')
    reg = r'class="mm-first" href="///(.*?)"'
    return re.findall(reg,html)


    #print html   输出测试
    #去掉页面的url多个参数以后，发现（https://mm.taobao.com/self/album_photo.htm?user_id=2925763379&album_id=10000935039）可以正常访问。按F12，查看network，XHR，点击左侧抓到资源，查看response，发现有对应的ID。

    for i in geturlList():
        userId = i['userId']
        #getInfo(userId)
        for n in getAlbumList(userId):
            print n
        break  #请求一次就停掉
        #print i['realName']  取到抓取页面的人名，也可以取其他的值，在preview选项下，searchDOList下，随意点开一个，可以看到他的其他可被抓取的项。 关注一下userid。根据分析网站，发现点开一个人的个人页面以后，userid是决定页面内容不同的一个重要部分，即访问（https://mm.taobao.com/self/aiShow.htm?userId=2925763379）这样的网址，一样可以获得其中一个人的个人界面。

print geturlList()
#geturlList()
#返回数据测试，发现有乱码的话，就要在网页的response headers中，content-type中，查看编码情况。或者在网页源码中查看编码情况。然后对数据进行转码。

'''
在分析相册图片的时候，
（https://img.alicdn.com/imgextra/i3/2925763379/TB1kjfiRpXXXXbvXVXXXXXXXXXX_!!0-tstar.jpg_290x10000.jpg）
（https://img.alicdn.com/imgextra/i3/2925763379/TB1kjfiRpXXXXbvXVXXXXXXXXXX_!!0-tstar.jpg_620x10000.jpg）
根据图片的URL，可以看到一些细微的差异。
如果去掉_620x10000.jpg这样的url参数，就是直接显示原图

'''


