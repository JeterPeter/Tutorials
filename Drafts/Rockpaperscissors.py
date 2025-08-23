import random

print("Let's play rock paper scissors! ")
pWins = 0
cWins = 0
pChoice = None
options = ["rock","paper","scissors","gun"]

def playerPick():
    global options
    global pChoice

    pChoiceTemp = input("What will you pick? ")
    #print("pchoicetemp is ", pChoiceTemp)
    if pChoiceTemp not in options:
        print("Invalid input! Pick again. Make sure to choose only rock, paper, or scissors")
        playerPick()
    else:
        return pChoiceTemp

def rps():

    global pWins
    global cWins
    global options
    global pChoice
    pChoice = None

    #define choices
    #random.seed()
    cChoice = options[random.randrange(0,3)]
    print("Computer's choice: ", cChoice, "\nThe computer has chosen!\n")
    
    pChoice = playerPick()
    #print("Player's choice is ",pChoice)
    #decide winner
    if (options.index(pChoice) > options.index(cChoice) and (options.index(pChoice)!=2 and options.index(cChoice)!=0)) or (options.index(pChoice)==0 and options.index(cChoice)==2):
        print("\nYou won this round!")
        pWins+=1
    elif options.index(pChoice) == options.index(cChoice):
        print("\nIt was a tie!")
    else:
        print("\nThe computer wins this time! ")
        cWins+=1
    
    #display current scores
    print("The computer currently has currently won ", cWins, " games.")

    #play again
    print("Would you like to play again?")
    if input("") == "yes":
        rps()
    else:
        print("Goodbye!")
        quit()

#starts the game
rps()
   
    



    