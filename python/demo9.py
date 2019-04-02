# 使用字符串来保存文字

strin = "fang"

# print(strin[1:])

# 下面是  and or not 的使用

v = 1;
print(not v, not v and v, not v and not v, not v or not v
      , not v or v)

# 常用的数据转换方法
print(int("10", 8))

# print(int("two"))
print("", type(v))

print(str((not True) and (not False)))

# 下面是元组,注意元组是中括号
tuple = (1, 34, 35, 647, [424, 646, 57])

# 下面是列表，注意列表是[]
lis1 = [12, 35, 64]

# 下面是字典
data = {
    "name": "fang",
    "age": 24,
    "Man": False
}
# 下面是集合
data1 = {"fang", "zhi", "yue"}

print(lis1.index(12))


# for i in range(1, 10):
#     for j in range(i, 10):
#         print("*")
#         pass
#     print("\n");

# try:
#     int("3526at")
# except TypeError:
#     print(TypeError.args);
#     pass


class fang:
    class demo:
        def demo1(self):
            print("asgadsgad")
            return fang();
            pass

    # 静态方法的注解
    @staticmethod
    def Fang():
        print("agadgad")
        pass


fang.demo().demo1();

# test = fang();
# demo1 = fang.demo();
# demo1.demo1();

# 我们发现内部类并不依赖于外部类的实现
# 我们在调用内部类的方法是，并不需要创建外部类的实例才能创建内部类的实例
# 也就是说，外部类默认是静态的

import builtins;


def demo3():
    pass


# builtins.staticmethod(demo3).__sizeof__()

# 我
# 们发现常用的系统函数，存放在builtins模块中

def demo4(num2, num=4):
    return num + num2;
    pass


def mode5(num2, num=None):
    return num;


name = None
age = None
sex = None
name = "fagaeg"
print(name)

print("计算的值是", demo4(12))

# 我们发现如果采用说的是None，那么在使用的时候可以不用赋值，同时
# 可以将任意值赋值过去

print("得到的新值是", mode5(12))

import re


# mat = re.match()


# 下面是继承的例子

class Fang:
    "这时我的姓"
    name = None
    age = None

    def __init__(self, sex):
        self.sex = sex;

    pass

    def _print(self):  # protected
        print("hahahav0")
        pass

    def __printColor(self):  # private
        print("zdbsdbsfghsfg")
        pass

    def printDemo(self):
        print("agagwegg")
        pass


class Zhi(Fang):
    "这是一个继承类的实现"

    def _print(self):
        pass

    # def __printColor(self):
    #     pass


Zhi("qwqe")._print();




import subprocess



