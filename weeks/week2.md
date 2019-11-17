# Week 2 - Intro to Turtle #

## Topics Covered ##

- Program control with while loops
- if, elif, else loop
- Importing and using python libraries

This week we played some more with Rock, Paper, Scissors. I shared an alternate version of the code that allows the player to keep playing until they press 'q' for Quit. When they finish, a score is printed to the console.

```text
rock(r), paper(p), scissors(s) or quit(q)? r
r  vs  p
Computer Wins!
rock(r), paper(p), scissors(s) or quit(q)? s
s  vs  r
Computer Wins!
rock(r), paper(p), scissors(s) or quit(q)? p
p  vs  s
Computer Wins!
rock(r), paper(p), scissors(s) or quit(q)? r
r  vs  p
Computer Wins!
rock(r), paper(p), scissors(s) or quit(q)? s
s  vs  p
Player Wins!
rock(r), paper(p), scissors(s) or quit(q)? q

Score
-----
Player:  3
Computer:  8
Draw:  3
```

## Turtle Race ##

We worked together on this project:
[Turtle Race](https://projects.raspberrypi.org/en/projects/turtle-race) Using this [Trinket](http://jumpto.cc/python-new)

![Turtle Race](../images/race-more.png)

```python
#!/bin/python3

from turtle import * #import everything from turtle
from random import randint #import only randint from random

speed(0) # the initial draw speed
penup() # raise the pen so it doesn't draw
goto(-140, 140) # move the pen to -140, 140

for step in range(15): # loop from 0 to 14
write(step, align='center') #write the step number and center it on the line
right(90) #turn right 90 degrees
for num in range(8): #draw a dashed line
    penup()
    forward(10)
    pendown()
    forward(10)
penup()
backward(160) # go back to the top
left(90)
forward(20) # move over 20

red = Turtle() # create a new turtle called red
red.color('red') # change red's color
red.shape('turtle') # change red's shape

for turn in range(100):
red.forward(randint(1,5)) # move red a random number forward
```

## Next Week ##

More with Turtles and if time permits Lists and Dictionaries
