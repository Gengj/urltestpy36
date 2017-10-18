#!/usr/bin/env python3

# encoding: utf-8

'''

@author: Gengj

@license: (C) Copyright 2013-2017.

@contact: 35285770@qq.com

@software: NONE

@file: test.py

@time: 17/10/17 下午11:33

@desc:

'''

from urllib import request

if __name__ == '__main__':

    req = request.Request('http://www.baidu.com')
    req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
    # 这里用Mac chrome浏览器找到的value太长了，伪造了一个window的
    # 原value如下：
    # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

    resp = request.urlopen(req)

    print(resp.read().decode("UTF-8"))
