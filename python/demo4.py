#!/usr/bin/python
# coding=UTF-8
# 发送http请求的模块
import requests


#  url = "https://kyfw.12306.cn/otn/login/init"
# 发送一个http请求，这里我们使用的cookie的保持
# 原因是我们发现我们在访问这个界面时，系统在响应头中实现了cookie的保持，也就是实现了对
# cookie的存储，我们为了实现同样的模拟，就需要实现同样的效果
def send_request(url):
    session = requests.Session();
    # 第一步请求页面
    # 上面的请求的地址是一个html，所以我们使用响应结果的文本显示
    response = session.get(url);
    print(response.text);


# 发送没有cookie的请求
def send_nocookie_request(url):
    response = requests.get(url);
    print(response.text);


# 第二部下载验证码，用来实现验证，因为我们在登录的过程中，我们发现需要
# 通过图片实现登录的验证，为了模拟这样的操作，我们就需要下载验证码的图片
def send_request_capture(url):
    session = requests.Session();
    # 第一步请求页面
    # 上面的请求的地址是一个图片，图片是一个二进制的数据，所以我们使用响应结果的二进制显示
    # 我们将图片写入文件中进行保存
    response = session.get(url);

    '''
     在这里response是response对象，代表的是http的响应对象
    '''


def write_file(name, response):
    f = open(name, "wb");  # 写二进制文件
    f.write(response.content);  # response对象的内容
    f.close();


'''
这里是我们对验证码的检查
我们使用的是表单的数据提交方式
为了解决数据的提交问题
我们使用字典
'''


def check_url(url):
    data = {
        'answer': '254,196',
        'login_site': 'E',
        'rand': 'sjrand'
    }
    session = requests.Session();
    check = session.post(url, data);
