#!/bin/python3

# pylint: disable-msg=E0611

from turtle import speed, penup, goto, write, right, pendown, forward, left, backward
# from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(15):
    write(step, align='center')
    right(90)
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)
