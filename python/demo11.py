#!/usr/bin/python
# coding=utf-8

str = "for i in range(0,10):" \
      "print(i)"
c = compile(str, '', "exec")
exec(c);

i = 0
seq = ["one", "two", "three"]
for i, element in enumerate(seq):
    print(i, " ", element);


def one():
    print("this is extern function");
    def inner_one_func():
        print("this is inner function");
        pass
    return inner_one_func;  # 在函数中返回一个函数
one()();  # 内部调用


def hi():
    return "hello world"
def doSomeFunc(func):
    func();
    pass
doSomeFunc(hi());



import  requests;
class MyRequest(object):
    '''
    这个类的作用是对requests的请求做的在此封装
    '''

    def simpleRequests(self,httpUri):
        r=requests.get(httpUri);
        r.text#请求的网页文本
        r.headers #请求的头
        r.encoding#编码
        r.status_code#请求的状态码
        p=requests.post(httpUri,)








