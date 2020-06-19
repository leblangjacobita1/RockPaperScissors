'''
Created on Jun 16, 2020

@author: ITAUser
'''

#set variable keepPlaying to true
keepPlaying = True
#While keepPlaying is true:
while (keepPlaying):

    #print statement welcoming players to the game
    print("Welcome to ROCK PAPER SCISSORS")
    
    #print statement stating the rules (best 2 out of 3, press 'q' to quit)
    print("  The rules are as follows:")
    print("  ROCK = 1, PAPER = 2, ")
    print("     SCISSORS = 3")
    print("    Best 2 out of 3")
    print("   press Q/q to quit")
    #make a key that assigns a number to  each choice for the computer
    #(rock is 1, scissors is 2, paper is 3)
    computerChoices = [1, 2, 3]
    #import the random functions
    import random
    #set computer's score to 0
    computerScore = 0
    #set player's score to 0
    playerScore = 0
    #while player's score is less than 2 and computer's score is less than 2:
    while ((playerScore < 2) and (computerScore < 2)):
    
        #computer's choice = random number between 1 and 3
        def randomChoice():
            random.randint[1, 4]
            print(randomChoice)
            return randomChoice
        #player's choice = input player to select Rock, Paper or Scissors
        playerChoice = choice_from_player()

        #else if (player inputs and computer chooses rock) or
            if (playerInput = (1)) and (randomChoice = (1)):
            print("TIED")
            print(playerScore)
            print(computerScore)
        #(player inputs paper and computer chooses paper) or
        else if (playerInput = (2) and randomChoice = (2)):
            print ("TIED")
            print(playerScore)
            print(computerScore)
        #(player inputs scissors and computer chooses scissors):
        else if (playerInput = (3) and randomChoice = (3)):
            print ("TIED")
            print(playerScore)
            print(computerScore)
        #   print out TIED
        
        #   print out player's score and computer's score
        
        #else if (player inputs rock and computer inputs scissors) or
        #(player inputs scissors and computer inputs paper) or
        #(player inputs paper and computer chooses rock):
        #   add one to the player's score
        #   print out player's score and computer's  score
        
        #else if (player inputs rock and computer paper) or
        #(player inputs scissors and computer chooses rock) or
        #(player inputs paper and computer scissors):
        #   add one to the computer's score
        #   print out player's score and computer's score
        
        #else:
        else:
        #   tell the user input was not valid
            print("ERROR: INVALID INPUT, TRY:")
            print("Rock, Paper, Scissors")