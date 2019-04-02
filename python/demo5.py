# !usr/bin/python
# coding=utf-8

import turtle

window = turtle.Screen();  # 创建一个新窗口用于绘图

babbage = turtle.Turtle();
babbage.color("green", "black");


# babbage.left(90);
# babbage.forward(100);
# babbage.right(90)
# babbage.color("green");
# babbage.circle(100);

# 下面开始绘制第一片树叶
# for i in range(1, 24):
#     if babbage.color() == ("red", "black"):
#         babbage.color("orange", "black")
#     elif babbage.color() == ("orange", "black"):
#         babbage.color("yellow", "black");
#     else:
#         babbage.color("red", "black");
#     babbage.left(15);
#     babbage.forward(50)
#     babbage.left(157);
#     babbage.forward(50);

# babbage.towards(200, 200)

# babbage.left(45)
# babbage.forward(100)
# babbage.right(45)
# babbage.forward(100)
# babbage.right(45)
# babbage.forward(100)
# babbage.right(45)
# babbage.forward(100)
# babbage.right(45)
# babbage.forward(100)
# babbage.right(45)
# babbage.forward(100)
# babbage.right(45)
# babbage.forward(100)

# 这是画八边形的
def drawRectf():
    for i in range(0, 8):
        babbage.right(45)
        babbage.forward(100)
        pass


# 这是画八边形的
def drawCircle():
    for i in range(0, 720):
        babbage.right(0.5)
        babbage.forward(1)
        pass


#
# drawRectf()

drawCircle()
babbage.hideturtle();
window.exitonclick();  # 单击窗口自动退




# for i in range(0, 24):
#     print("输出的值是", i);


# class myPhone:

#     '这是我的手机的测试类'
#
#     def printInfo(self):
#         pass
#
#     def __init__(self):
