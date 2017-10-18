#!/usr/bin/env python3

# encoding: utf-8

'''

@author: Gengj

@license: (C) Copyright 2013-2017.

@contact: 35285770@qq.com

@software: NONE

@file: test2.py

@time: 17/10/18 上午12:45

@desc:

'''
import urllib
from urllib import request
from urllib import parse

req = urllib.request.Request('http://www.thsrc.com.tw/tw/TimeTable/SearchResult')

postData = urllib.parse.urlencode([
    ("StartStation", "977abb69-413a-4ccf-a109-0272c24fd490"),
    ("EndStation", "5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f"),
    ("SearchDate", "2017/10/20"),
    ("SearchTime", "06:00"),
    ("SearchWay", "DepartureInMandarin")
])

req.add_header("Origin", "http://www.thsrc.com.tw")
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')

reps = request.urlopen(req, data=postData.encode("utf-8"))
#req加上两个header以后，和postData（实际是body）
#一起让request对象使用urlopen方法post给指定的地址

print(reps.read().decode("UTF-8"))
#返回的reps（响应）使用read方法讲网站响应的数据读出来

