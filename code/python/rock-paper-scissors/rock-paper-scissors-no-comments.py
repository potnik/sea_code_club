#!/bin/python3

from random import randint

play = True 
draw = 0
pw = 0 
cw = 0 

while play==True:
  prompt = True
  while prompt == True:
    player = input('rock(r), paper(p) or scissors(s)?')
    if player=='r' or player=='s' or player=='p':
      prompt=False
    else:
      print('Please enter r, p, or s')

  chosen = randint(1,3)
  
  if chosen == 1:
    computer = 'r'
  elif chosen == 2:
    computer = 'p'
  else: 
    computer = 's'

  print(player, ' vs ', computer)

  if player == computer:
    print('DRAW!')
    draw = draw + 1
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

  again=input('Play again? enter q to quit')
  if again=='q':
    play=False  

  print()
  print('Score')
  print('-----')
  print('Player: ', pw)
  print('Computer: ', cw)
  print('Draw: ', draw)
  print()
