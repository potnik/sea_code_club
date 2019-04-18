# Week 9 – Into to Python Console and Code Craft

For week 9, we reviewed the code we did wrote for the ISS Tracker; we looked at the Python Console for testing code snippets and then took on a very complex project -- Code Craft -- a 2D version of Minecraft written in Python.

One of the topics we discussed is the two ways to import a module into python and the pros and cons:

```python
import turtle
import random

# the module name is needed every time
yertle = turtle.Turtle()
randnum = random.randint(1, 3)
```
This first method keeps your import statements short but you have to reference the module name each time.

```python
from turtle import *
from random import randint

# no module name needed
yertle = Turtle()
randnum = randint(1, 3)
```
This second method is a little more wordy up front, but you can be more specific about the parts of the module you want to import (randint from random) and it saves you from having to type the module name every time.

