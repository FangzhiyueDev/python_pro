#! /usr/bin/python
# ! coding=utf-8
#
# person = {"name": "fang", "age": "12", "address": "anhui"}
#
# for key, value in person.items():
#     print("key:%s   value:%s" % (key, value))


def fang():
    try:
        fang = 12 / 0;
    except BaseException as e:
        print(e.args)
    else:
        print("执行成功")
    finally:
        print("执行结束")


class MyNumber:

    def __iter__(self):
        self.n = 0;
        return self;

    def __next__(self):
        if self.n < 200:
            self.n += 1;
        else:
            raise StopIteration
        return self.n;


# 迭代器，用来实现对类的迭代处理
# 必须实现__iter__()方法与__next()


# var = iter(MyNumber());
# print(next(var))
# print(next(var))
# print(next(var))


# for ev in iter(MyNumber()):
#     print(ev)


def value(end):
    var = 0;
    while var < end:
        yield var
        var += 1


# for var in value(12):
#     print(var)


def myPrint(*argc, speed=None, rate=None):
    var = argc;
    for ele in var.__iter__():
        print(ele)


#
# myPrint(("35235", "35", "353"))

# print(("sdgsd", "dhs", 434))


def callback(person):
    print("姓名", person.getName());
    print("年龄", person.getAge());


class Person():
    __name = "";
    __age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def getName(self):
        return self.__name

    @property
    def getAge(self):
        return self.__age


def myLIstener(name="", age=0, challback=None):
    innerName = name;
    innderAA = age;
    challback(Person(innerName, innderAA));





