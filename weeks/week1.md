# Week 1 - Welcome to Code Club

Thanks for coming to our first Code Club meeting.  I started Code Club to give students a chance to move beyond Scratch and other graphical coding environments.  In Code Club, you will be typing code -- so much typing...

This year in SEA Code Club, we will be working with the Python programming language.  Python is a full powered and popular development language.

While there a lots of resources available for Python 2 (2.7), everything we will be doing will be Python 3 since Python 2 will be obsolete next year.

There are some differences between them--enough that Python 2 code will not always run in a Python 3 environment without rewriting it (know as refactoring).

This week we set up with our Trinket.io accounts and learned to navigate around the development environment.  We spent a lot of time typing in the Python console.  The console is a great place to test one or more lines of code (sometimes called a snippet), before putting them into a lengthy program.

We worked through as many of the python language basics as we could in an hour. We followed along with the lessons here:

<https://docs.trinket.io/getting-started-with-python#/welcome/where-we-ll-go>

  These included:

- Numbers
- Logic
  - Booleans (TRUE and FALSE)
- Words and letters
  - Strings
  - Changing text
- Variable containers
  - Variables
  - User input

## Project of the Week

We started coding Rock, Paper Scissors <https://projects.raspberrypi.org/en/projects/rock-paper-scissors>

In Trinket, we start all our scripts with a Python 3 Shebang!: **#!/bin/python3**

This tells Trinket that we are using Python 3 syntax and not Python 2

Then, we used our first **import** statement:

```python
from random import randint
```

There are many commands "built in" to python like the print() function we used or the basic math and string functions we worked with.  But many times you have to **import** functionality.  In this case, we imported the random integer generation function called **randint**

The last thing we covered before we ran out of time is the **input** function.  This is how we prompt a user for a value we can use in our program.  In this case, we were prompting for their choice in Rock, Paper, Scissors:

```python
player = input('rock(r), paper(p), scissors(s)')
```

Here is the completed code:

```python
#!/bin/python3

from random import randint
  
player = input('rock (r), paper (p) or scissors (s)?')

if(player == 'r'):
  print('O', end=' ')
  
elif(player == 'p'):
  print('___', end=' ')
  
elif(player == 's'):
  print('>8', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')

chosen = randint(1,3)

if(chosen == 1):
  computer = 'r'
  print('O')
  
elif(chosen == 2):
  computer = 'p'
  print('___')
  
else:
  computer = 's'
  print('>8')

if(player == computer):
  print('DRAW!')
  
elif(player == 'r' and computer == 's'):
  print('Player wins!')
  
elif(player == 'r' and computer == 'p'):
  print('Computer wins!')
  
elif(player == 'p' and computer == 'r'):
  print('Player wins!')
  
elif(player == 'p' and computer == 's'):
  print('Computer wins!')

elif(player == 's' and computer == 'p'):
  print('Player wins!')
  
elif(player == 's' and computer == 'r'):
  print('Computer wins!')

else:
  print('Huh?')
  
  
```

## Next Week

We'll continue with Rock, Paper Scissors looking at ways to make it better and introduce:

- Conditionals
  - If statements
  - Nested if statements
- Loops
  - While loops
  - For loops
