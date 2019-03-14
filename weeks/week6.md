# Rock, Paper, Scissors

This week, we created a simple game of Rock, Paper, Scissors.  This lesson re-visited some concepts we worked with in our Turtle race project. We'll cover more of this in depth during week 6.

We revisited importing modules by importing the **randint** function from **random**

 ```python
 from random import randint
 ```
 We learned about the **input** command and how to use it to prompt a user for a response and then use that response to drive our program:

```python
 player = input('rock (r), paper (p) or scissors (s)?')
```
Next we generated a random value between 1 and 3 inclusive to use to determine the computer response:

```python
chosen = randint(1,3)
```

And then a series of if, elif, else statements to determine who wins:

```python
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
  
elif(player == "s" and computer == 'r'):
  print('Computer wins!')

else:
  print('Huh?')
```

But we also learned that a more efficient way to code this is:

```python
if player == computer:
      print('DRAW!')
    elif player == 'r' and computer == 's':
      print('Player Wins!')
    elif player == 'p' and computer == 'r':
      print('Player Wins')
    elif player == 's' and computer == 'p':
      print('Player Wins!')
    else:
      print('Computer Wins!')
```
