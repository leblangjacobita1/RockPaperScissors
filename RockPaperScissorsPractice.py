import random

def randomChoice():
    random.choice ( ["Rock", "Paper", "Scissors"] )
   

    return random.choice

keepPlaying = True
computerScore = 0
playerScore = 0
while keepPlaying == True:

    print("Welcome to Rock Paper Scissors!")
    print("The rules are simple. Best 2 out of 3, and you can press Q or q to quit anytime")
    
while (computerScore < 2 and playerScore < 2):
    playerInput = input ("Pick Rock, Paper, or Scissors")
    print( "Player has picked" + playerInput)
    computerInput = print ("Computer has picked" + randomChoice)
    if((computerInput = "Rock") and (playerInput = "Rock")):
        print("TIED")
    else
    if(computerInput = "Paper" and playerInput = "Paper"):
        print("TIED")
    else
    if(computerInput = "Scissors" and playerInput = "Scissors"):
        print ("TIED")
    else
    if(computerInput = "Paper" and playerInput = "Rock")
        print ("COMPUTER WINS")
        computerScore = computerScore + 1
    else
    if(computerInput = "Scissors" and playerInput = "Paper")
        print("COMPUTER WINS")
        computerScore = computerScore + 1
    else
    if(computerInput = "Rock" and playerInput = "Scissors")
        print("COMPUTER WINS")
        computerScore = computerScore + 1
    else
    if(playerInput = "Paper" and computerInput = "Rock")
        print("PLAYER WINS")
        playerScore = playerScore + 1
    else
    if(playerInput = "Rock" and computerInput = "Scissors")
        print("PLAYER WINS")
        playerScore = playerScore + 1
    else
    if(playerInput = "Scissors" and computerInput = "Paper")
        print("PLAYER WINS")
        playerScore = playerScore + 1
    else
    print("ERROR, INVALID INPUT")
    
    if(playerInput = "Q" or playerInput = "q")
        print("Goodbye, Thanks for Playing!")
        keepPlaying = False
    if(playerScore > 2)
        print("You Won! Nice work!")
    if(computerScore > 2)
        print("The computer won! Better luck next time!")