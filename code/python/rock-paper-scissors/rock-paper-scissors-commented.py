#!/bin/python3

# The previous line looks like a comment, but is known as a shebang
# it must be the first line of the file.  It tells the computer that
# this is a python script and to use python3 found in the /bin folder

from random import randint
# From the python module called random, import the function randint
# randint returns a random integer in range [a, b], including both end points.

# initiate some variables an assign them values
play = True # this will be used to keep the game going if the user chooses to

# These next three are to hold the score for reporting later
draw = 0  # number of draw games
pw = 0 # number of player wins
cw = 0 # number of computer wins

# The main part of the program consists of a while loop that runs the game
# until the player tells it to quit
while play==True: # while the value of the variable play equal True, keep running the game loop
  prompt = True # set the prompt variable to True
  while prompt == True: # keep prompting the player until they give the correct response
    player = input('rock(r), paper(p) or scissors(s)?')
    if player=='r' or player=='s' or player=='p':
      prompt=False
    else:
      print('Please enter r, p, or s')

  # Here we use randint to generate an integer. In this case, 1, 2, or 3
  # this will map to the computers selection below
  chosen = randint(1,3)

  # A comment to remind us what each value means.  Commenting you code is a good practice
  # 1 = rock (r)
  # 2 = paper (p)
  # 3 = scissors (s)
  
  # an if, elif, else block that assigns a letter to the value of chosen
  if chosen == 1:
    computer = 'r'
  elif chosen == 2:
    computer = 'p'
  else: # an else statement doesn't have a condition.
    computer = 's'
    
  print(player, ' vs ', computer)
  
  # A block of if statements to determine who wins
  if player == computer:
    print('DRAW!')
    draw = draw + 1 # these statements keep a running count of the score
  elif player == 'r' and computer == 's':
    print('Player Wins!')
    pw = pw + 1
  elif player == 'p' and computer == 'r':
    pw = pw + 1
    print('Player Wins')
  elif player == 's' and computer == 'p':
    pw = pw + 1
    print('Player Wins!')
  else:
    print('Computer Wins!')
    cw = cw + 1

  # prompt the user if they want to play again.
  # if they enter anything other than q, continue
  again=input('Play again? enter q to quit')
  if again=='q':
    play=False  

  # Finally, print out the scoreboard 
  print()
  print('Score')
  print('-----')
  print('Player: ', pw)
  print('Computer: ', cw)
  print('Draw: ', draw)
  print()
