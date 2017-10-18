#!/usr/bin/env python
# encoding: utf-8

'''
@author: Gengj
@license: (C) Copyright 2013-2017.
@contact: 35285770@qq.com
@software: NONE
@file: bsTest.py
@time: 17/10/18 下午7:37
@desc:
'''

from bs4 import BeautifulSoup as bs
# import html.parser
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
if __name__ == '__main__':
    soup = bs(html_doc,"html.parser")
    # print(soup.prettify())
    # print(soup.title.string)
    # print(soup.a)
    # print(soup.find(id = "link2").string)
    # print(soup.findAll("a"))
    #
    # for link in soup.findAll("a"):
    #     print(link.string)
    # for tag in soup.find_all("^b"):
    #     print(tag.name)

    data = soup.findAll("a",href = re.compile(r"http://example\.com/"))
    # data2 = soup.findAll()
    print(data)
