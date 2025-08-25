import pig

def game():
    scores = {}
    winScore = 0
    winner = False

    playerCount = abs(int(input("How many players are playing? \n")))

    i = 0
    while i<playerCount:
        player = "Player " + str(i+1) + ", what is your name?\n"
        scores.update({input(player):0})
        i+=1
    print(scores)

    winScore = int(input("\nTo what score will you play? \n"))
    keys = pig.keysToList(scores.keys())

    while winner != True:

        
        for x in keys: 
            
            print("\nIt is ", x, "'s turn!")
            print("\nYour score is currently ", scores[x], "\n")
            scores[x] = scores[x] + pig.turn()
            
            
            #if player score > winScore then player wins by setting winner to true 
            if scores[x] >= winScore:
                print("\n\n", x, "won the game! Get dunked on, losers!")
                winner = True
                break
            #x+=1

    print("Game over\n\n")
    
#runs the game
playing = True
while playing == True:
    game()
    #print("Game run!")

    continuePlaying = input("Would you like to play again? (yes/no)\n")

    if  continuePlaying == "yes":
        pass
    elif continuePlaying == "no":
        playing = False
    else:
        print("Invalid input. Game ending...")
        playing = False

print("Thanks for playing!")


