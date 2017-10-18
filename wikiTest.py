#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Gengj
@license: (C) Copyright 2013-2017.
@contact: 35285770@qq.com
@software: NONE
@file: wikiTest.py
@time: 17/10/18 下午8:13
@desc:
'''

from urllib.request import urlopen
import re
from bs4 import BeautifulSoup


if __name__ == '__main__':
    # req = request.Request('https://en.wikipedia.org/wiki/Main_Page')
    # req.add_header("user-agent", "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)")
    # reps =

    # print(reps.read().decode("UTF-8"))

    reps = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
    soup = BeautifulSoup(reps,"html.parser")
    print(soup)

