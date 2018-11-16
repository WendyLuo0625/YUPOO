#!/usr/bin/python

import re
import os
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getUrl(html):
  #  ureg = r'href=\/photos\/"(.*?)"\/uid=1'
    ureg = r'href="(\/photos\/.*\?uid=1)"'
    treg = r'text_overflow album__title\">(.+i?)</div>'
    urlre = re.compile(ureg)
    titlere = re.compile(treg)
    urllist = re.findall(urlre, html)
    titlelist = re.findall(titlere, html)
    return titlelist,urllist

def getDes(html):
    pass

def getImg(url,title):
    reg = r'data-origin-src="(.*?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, url)
    #create seprate folder
    path = title
    #os.makedirs(path)
    x = 0
    for imgurl in imglist:
        imgurl = 'http:'+imgurl
        urllib.urlretrieve(imgurl, "%s.jpg" %x)
        x+=1

url=getHtml("http://x.yupoo.com/photos/zoestreet/albums?tab=gallery")
t_u = getUrl(url)

l = 0 
for t in t_u:
    #getImg(urls[l],titles[l])
    print(t)
    l+=0

#print(len(getUrl(url)[0]))
#print(len(getUrl(url)[1]))

