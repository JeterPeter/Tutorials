
import random
cWins = 0
pWins = 0
cChoice = None
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
        pChoice = options.index(pChoiceTemp) + 1
        return

def rps():
    global options
    global cChoice
    global pChoice
    global pWins
    global cWins
    
    i = 0
    while i < 1:
        #determine choices
        cChoice = random.randrange(1,4)
        print("The computer has chosen ", cChoice)
        print("The computer has chosen!\n")
        playerPick()
        print("the player has chosen ", pChoice, "\n\n")


        #victory algorithm
        if cChoice == pChoice:
            print("It was a tie!")
        elif pChoice == 4:
            print("the player wins!")
            pWins+=1
        elif cChoice == 1 and pChoice == 2:
            print("the player wins!")
            pWins+=1
        elif cChoice == 1 and pChoice == 3:
            print("The computer wins this round!")
            cWins+=1
        elif cChoice == 2 and pChoice == 3:
            print("the player wins!") 
            pWins+=1
        elif cChoice == 2 and pChoice == 1:
            print("The computer wins this round!")
            cWins+=1
        elif cChoice == 3 and pChoice == 1:
            print("the player wins!")
            pWins+=1
        elif cChoice == 3 and pChoice == 2:
            print("The computer wins this round!")
            cWins+=1
        else:
            print("error")
        
        if input("\ndo you want to play again?(yes/no) \n") != "yes":
            i+=1

rps()   


print("game over")
print("You won ", pWins, " games")
quit()