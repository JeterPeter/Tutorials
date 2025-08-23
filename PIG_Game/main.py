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

winScore = int(input("\nTo what score will you play? \n"))

while winner != True:
    x = 0
    while x < playerCount:
        #turn(player) (returns the score a player receives this turn)
        print("\nIt is player ", x+1, "'s turn!")
        print("\nYour score is currently ", scores[x], "\n")
        scores[x] = scores[x] + pig.turn()
        
        
        #if player score > winScore then player wins by setting winner to true 
        if scores[x] >= winScore:
            print("\n\nPlayer ", x+1, " won the game! Get dunked on, losers!")
            winner = True
            break
        x+=1

print("Game over")
    
    

