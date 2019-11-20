#!/bin/python3

from turtle import speed, penup, goto, write, \
    right, pendown, forward, left, backward, Turtle
from random import randint
import time

speed(0)
penup()
goto(-140, 140)

for step in range(16):
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

ada = Turtle()
ada.color("red")
ada.shape("turtle")

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color("blue")
bob.shape("turtle")

bob.penup()
bob.goto(-160, 70)
bob.pendown()

joe = Turtle()
joe.color("orange")
joe.shape("turtle")

joe.penup()
joe.goto(-160, 40)
joe.pendown()

sue = Turtle()
sue.color("purple")
sue.shape("turtle")

sue.penup()
sue.goto(-160, 10)
sue.pendown()

a_score = 0
b_score = 0
j_score = 0
s_score = 0

for turn in range(110):
    a = randint(1, 5)
    b = randint(1, 5)
    j = randint(1, 5)
    s = randint(1, 5)

    ada.forward(a)
    bob.forward(b)
    joe.forward(j)
    sue.forward(s)

    a_score = a_score + a
    b_score = b_score + b
    s_score = s_score + s
    j_score = j_score + j

winner = Turtle()

winner.penup()
winner.goto(-140, -50)
winner.pendown()
winner.shape('turtle')

if a > b:
    if a > j:
        if a > s:
            winner.color('red')
            winner.write('Ada Wins!', font=('Arial', 18, 'normal'))
elif b > j:
    if b > s:
        winner.color('blue')
        winner.write('Bob Wins!', font=('Arial', 18, 'normal'))
elif j > s:
    winner.color('orange')
    winner.write('Joe Wins!', font=('Arial', 18, 'normal'))
else:
    winner.color('purple')
    winner.write('Sue Wins!', font=('Arial', 18, 'normal'))

winner.penup()
winner.goto(-140, -100)

print('Scores')
print('---------------------')
print('ada: ' + str(a_score))
print('bob: ' + str(b_score))
print('joe: ' + str(j_score))
print('sue: ' + str(s_score))

time.sleep(10)
