#!/usr/bin/python

import re
import os
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getDes(html):
    pass

def getImg(html):
    reg = r'data-origin-src="(.*?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        imgurl = 'http:'+imgurl
        urllib.urlretrieve(imgurl, "%s.jpg" %x)
        x+=1

html =  getHtml("http://x.yupoo.com/photos/zoestreet/albums/39807974?uid=1")
print(getImg(html))

