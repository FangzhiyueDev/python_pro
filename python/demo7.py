#!usr/bin/python
# coding=utf-8

import turtle
import time
import this

boxSize = 200
caught = False
score = 0
this


def up():
    mouse.forward(10)
    checkbound()


def left():
    mouse.left(5)
    mouse.forward(10)


def right():
    mouse.right(5)
    mouse.forward(10)


def back():
    mouse.backward(10)
    checkbound()


def quitTurtles():
    window.bye()


def checkbound():
    global boxSize
    if mouse.xcor() > boxSize:
        mouse.goto(boxSize, mouse.ycor())
    if mouse.xcor() < -boxSize:
        mouse.goto(-boxSize, mouse.ycor())
    if mouse.ycor() > boxSize:
        mouse.goto(mouse.xcor(), boxSize)
    if mouse.ycor() < -boxSize:
        mouse.goto(mouse.xcor(), -boxSize)


# set up screen
window = turtle.Screen()
mouse = turtle.Turtle()
cat = turtle.Turtle();
mouse.penup()
mouse.penup()
mouse.goto(100, 100)

# add key listeners
window.onkeypress(up, "Up")
window.onkeypress(left, "Left")
window.onkeypress(right, "Right")
window.onkeypress(quitTurtles, "Escape")

difficulty = window.numinput("Difficulty", "Enter a difficulty from easy (1),for hard (5)"
                             , minval=1, maxval=5)
window.listen()

while not caught:
    cat.setheading(cat.towards(mouse))
    cat.forward(8 + difficulty)
    score = score + 1
    if cat.distance(mouse) < 5:
        caught = True
    time.sleep(0.2 - (0.01 * difficulty))
window.textinput("Game Over", "Well done ,you scroed:" + str(score * difficulty))

window.bye()
