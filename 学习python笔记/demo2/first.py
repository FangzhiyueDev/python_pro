#! /usr/bin/python
# !coding=utf8

import urllib.response
import urllib.request
import urllib.parse
import urllib.error


def requestGet():
    """
    这个方法使用的是get请求发送数据
    :return:
    """
    url = "http://www.baidu.com/s?wd="
    key = "北京"
    keyQuote = urllib.request.quote(key)
    urlAll = url + keyQuote
    req = urllib.request.Request(urlAll)
    data = urllib.request.urlopen(req).read()
    with open("/home/fang/baidu.html", "wb") as f:
        f.write(data)


def requestPost():
    """
    这个方法的作用是执行post请求，同时设置了部分的请求头
    :return:
    """
    url = "http://www.iqianyue.com/mypost/"
    postdata = urllib.parse.urlencode({
        "name": "ceo@iqianyue.com",
        "pass": "aA123456"
    }).encode("utf-8")  # 对上面的参数进行编码
    req = urllib.request.Request(url, postdata)
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0")
    data = urllib.request.urlopen(req).read()
    with open("/home/fang/mypost.html", "wb") as f:
        f.write(data)


class MyRequest:
    """
    这个类封装了一些对代理服务发送网络请求的实现
    """

    def requestWithProxy(self, proxy_addr, url):
        """
        通过代理服务器发送请求
        :param  proxy_addr
        代理服务器的地址  下面是一些代理服务器的地址    <a href='http://www.xicidaili.com/'><a>
        :param url
        请求的网址
        :return:
        函数会将创建的html网页的信息存放到/home/fang/requestWithProxy.html中
        """
        proxy = urllib.request.ProxyHandler({
            "http": proxy_addr
        })
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read()
        with open("/home/fang/requestWithProxy.html", "wb") as f:
            f.write(data)

    def debugRequestTest(self):
        """
        开启调试模式进行网络请求的调试
        :return:
        """
        httphd = urllib.request.HTTPHandler(debuglevel=1)
        httpshd = urllib.request.HTTPSHandler(debuglevel=1)
        opener = urllib.request.build_opener(httphd, httpshd)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen("http://edu.51cto.com").read()
        with open("/home/fang/debugRequestTest.html", "wb") as f:
            f.write(data)

    def exceptionThrows(self):
        """
        异常处理请求

        :return:
        """
        try:
            urllib.request.urlopen("http://blog.csdn.net")
        except BaseException as e:
            print(e.args)


"""
下面是对正则表达式的学习
"""

import re


def demo1():
    pattern = "python"
    string = "i love python"
    result = re.search(pattern, string);

    print(result)


"""
下面是进行cookie的学习,
"""


def no_cookie_login_test():
    url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=L768q"
    postData = urllib.parse.urlencode({
        "username": "weisuen",
        "password": "aA123456"
    }).encode("utf-8")  # 使用urlencode编码后,再设置为utf-8编码
    req = urllib.request.Request(url, postData)
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0")
    data = urllib.request.urlopen(req).read()
    fhandle = open("post.html", "wb")
    fhandle.write(data)
    fhandle.close()

    # 上面的操作是用来进行登录用的,但是我们的cookie死不能保持的,在下次请求时本以为会爬取登录过后的相关信息,结果却不是
    # 由于cookie不能保持,在下次请求时,浏览器并不知道你是否已经进行了登录,这时我们爬取的依然是没有登录的页面信息

    url2 = "http://bbs.chinaunix.net/"  # 设置要爬取该网页下其他网页地址
    req2 = urllib.request.Request(url2, postData)
    req2.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0")
    data2 = urllib.request.urlopen(req2).read()  # 爬取该网页下面的其他网页
    fhandle = open("postother.html", "wb")
    fhandle.write(data2)
    fhandle.close()


"""
进行登录保持,我们需要对cookie进行设置
 1.导入cookie处理模块 http.cookirjar
 2.使用http.cookiejar.CookieJar()创建cookiejar对象
 3.使用HTTPCookieProcessor创建cookie处理器,并以其为参数构建opener对象
 4.创建全局默认的opener对象
"""
import http.cookiejar


def cookie_login_test():
    url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=L768q"
    postData = urllib.parse.urlencode({
        "username": "weisuen",
        "password": "aA123456"
    }).encode("utf-8")  # 使用urlencode编码后,再设置为utf-8编码
    req = urllib.request.Request(url, postData)
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0")
    # 使用http.cookiejar.CookieJar()创建CookieJar对象
    cjar = http.cookiejar.CookieJar();

    # 使用HTTPCookieProcessor创建cookie处理器, 并以其为参数构建opener对象
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
    # 将opener安装为全局
    urllib.request.install_opener(opener)
    file = opener.open(req)
    data = file.read()
    file = open("post.html", "wb")
    file.write(data)
    file.close()

    url2 = "http://bbs.chinaunix.net/"
    data2 = urllib.request.urlopen(url2).read()
    fhandle = open("postother.html", "wb")
    fhandle.write(data2)
    fhandle.close()


"""
图片爬虫实战
"""


def craw(url, page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div id="plist".+? <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    path2 = '<img  width="220" height="220" data-img="1" data-lazy="//(.+?\.jpg)">'
    imageList = re.compile(path2).findall(result1)
    x = 1
    for imageurl in imageList:
        imagename = "img" + str(page) + str(x) + ".jpg"
        imageurl = "http://" + imageurl
        try:
            urllib.request.urlretrieve(imageurl, filename=imagename)
        except urllib.error.URLError as  e:
            if (hasattr(e, "code")):
                x += 1
            if (hasattr(e, "reason")):
                x += 1
        x += 1


for i in range(1, 79):
    url = "http://list.jd.com/list.html?cat=9987,655,655&page=" + str(i)
    craw(url, i)

"""
链接爬虫实战
"""


# 爬取页面链接
def getlink(url):
    # 模拟浏览器
    headers = ("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 将opener安装为全局
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    # 根据需求构建链接表达式
    pat = '(https?://[^\s)";]+\.(\w|/)*'
    link = re.compile(pat).findall(data)
    # 去除重复的元素
    link = list(set(link))
    return link

# 要爬取的网页链接
url = "http://blog.csdn.net"
file = urllib.request.urlopen(url)













if __name__ == '__main__':
    demo1()




