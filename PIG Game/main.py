import pig

scores = []
winScore = 0
winner = False

playerCount = abs(int(input("How many players are playing? \n")))

i = 0
while i<playerCount:
    scores.append(0)
    i+=1
print(scores)

winScore = input("\nTo what score will you play? \n")

while winner != True:
    for i in scores:
        #turn(player) (returns the score a player receives this turn)
        print("It is player ", i, "'s turn!")
        scores[i] = scores[i] + pig.turn()
        
        #if player score > winScore then player wins by setting winner to true 
        if scores[i] >= winScore:
            winner = True
            print("Player ", i, " won the game! Get dunked on, losers!")
        #also break the for loop\
print("Game over")
    
    

