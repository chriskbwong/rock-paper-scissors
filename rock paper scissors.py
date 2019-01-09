'''
simple rock paper scissors game taught to 5th graders 
the program will allow them to play against another person, or a bot. 
teaches conditionals, loops, input, and random
'''
player = input("1 or 2 players?")

if (player == 1):
  print("not yet!")

else: 
  play = True
  while(play):
    player1 = input("Enter rock, paper, or scissors: ")
    if (player1) == "rock":
      brain = 1
    elif (player1) == "paper":
      brain = 2     
    else: 
      brain = 3

    player2 = input("Enter rock, paper, or scissors: ")
    if (player2) == "rock":
      heart = 1
    elif (player2) == "paper":
      heart = 2     
    else: 
      heart = 3
    
    if (brain == 1 and heart == 1):
      print("It was a tie! Play again!")
    elif (brain == 2 and heart == 2):
      print("It was a tie! Play again!")
    elif (brain == 3 and heart == 3):
      print("It was a tie! Play again!")

    elif(brain == 2 and heart == 1):
      print("Player 1 wins!")
      play = False  
    elif(brain == 3 and heart == 2):
      print("Player 1 wins!")
      play = False        
    elif(brain == 1 and heart == 3):
      print("Player 1 wins!")
      play = False 

    elif(brain == 1 and heart == 2):
      print("Player 2 wins!")
      play = False  
    elif(brain == 2 and heart == 3):
      print("Player 2 wins!")
      play = False        
    else:
      print("Player 2 wins!")
      play = False 
