# Week 5 - More Python, More Turtles

This week we finished the Turtle Race project working more with loops and random numbers.  So far, we've only used 'for' loops--**for something, in something, do something**:

``` python
for turn in range(10): # for turn in range 0-9
    red.right(36) # turn the turtle right 36 degrees
```
Keep in mind that the first line of a loop ends in a colon **:** and any statements you want in your loop need to be indented evenly:
```python
for i in range(10): #end in colon
    statement 1
    statement 2
        statement 3 # this will throw an error
statement 4 # this is outside the loop
```
You can find the final code in the code folder of this repo: [turtle-race.py](../code/python/turtle-race.py)