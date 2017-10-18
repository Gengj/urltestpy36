# -*- coding:utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import ssl
import re
if __name__ == '__main__':

    ssl._create_default_https_context = ssl._create_unverified_context
    # －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
    #这条SSL证书真坑爹啊，花了一个晚上时间搞明白报错在哪。报错如下：
    #urlopen ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify fa
    #Python 升级到 2.7.9 之后引入了一个新特性，当使用urllib.urlopen打开一个 https 链接时，会验证一次 SSL 证书。
    # 而当目标网站使用的是自签名的证书时就会抛出一个 urllib2.URLError: 的错误消息，
    # 详细信息可以在这里查看（https://www.python.org/dev/peps/pep-0476/）。
    # －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－

    #请求URL并把结果用UTF-8格式编码
    resp = urllib.request.urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode("UTF-8")

    #使用BeautifulSoup解析
    soup = BeautifulSoup(resp, "html.parser")


    #获取所有以/wiki/开头的a标签的href属性
    listUrls = soup.findAll("a",href = re.compile("^/wiki/"))
    for url in listUrls:
        if not  re.search("\.(jpg|JPG)$",url["href"]):
            print(url.get_text(),"<------->","https://en.wikipedia.org"+url["href"])
            #或者url.string（只能获取一个），get_text可以获取标签下所有文字

    # CurrentPageList = []
