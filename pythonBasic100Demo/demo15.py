# !/usr/bin/pyhton

import math


def demo1():
    for i in range(1, 5):
        for j in range(1, 5):
            for z in range(1, 5):
                if (i != z) and (j != z) and (i != j):
                    print(i, j, z);


def demo2():
    i = int(input("净利润"))

    arc = [1000000, 600000, 400000, 200000, 100000, 0]

    rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0

    for index in range(0, 6):
        if i > arc[index]:
            r += (i - arc[index]) * rate[index]
            i = arc[index]
        pass
    print("总金额", r, "人民币");


def demo3():
    for i in range(0, 10000):
        x = int(math.sqrt(i + 100))
        y = int(math.sqrt(i + 268))
        if (x * x == i + 100) and (y * y == i + 268):
            print(i)


def demo4():
    year = int(input("年份"))
    month = int(input("月份"))
    day = int(input("天数"))

    days = 0;
    months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    if month > 0 and month <= 12:
        days = months[month - 1]
    days += day
    leap = 0;
    if (year % 400 == 0) and ((year % 4 == 0) or (year % 100 != 0)):
        leap = 1
    if (leap == 1) and (month > 2):
        days += 1
    print("it is the ", days, "th day")


def demo5():
    l = []
    for i in range(0, 3):
        x = int(input("integer number"))
        l.append(x)
        pass
    l.sort()
    print(l)


def demo6():
    a = 0
    b = 1
    size = 0
    c = int(input("integer number"))
    print(a, b)
    for i in range(0, c - 1):
        value = a + b  # 得到的是下一项的值[1,2,]
        a = b
        b = value
        size += value
        print(value)
    print("数列的值为", size)


def demo7(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        return demo7(n - 1) + demo7(n - 2)


def demo8():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("ixj=", i * j, end='  ')
        print("")


if __name__ == '__main__':
    demo8()
