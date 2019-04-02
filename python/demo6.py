#!usr/bin/python
# coding=utf-8

import turtle
import time

boxSize = 200
caught = False
score = 0

# set up screen
window = turtle.Screen()
mouse = turtle.Turtle()
cat = turtle.Turtle();
mouse.penup()
mouse.penup()
mouse.goto(100, 100)

# add key listeners
window.onkeypress(up, "up")


def checkbound():
    global boxSize
