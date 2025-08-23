import pig

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

    
    for x in keys: #if the for loop doesn't work, put while x < len(keys) and activate x+=1
        #turn(player) (returns the score a player receives this turn)
        print("\nIt is ", x, "'s turn!")
        print("\nYour score is currently ", scores[x], "\n")
        scores[x] = scores[x] + pig.turn()
        
        
        #if player score > winScore then player wins by setting winner to true 
        if scores[x] >= winScore:
            print("\n\nPlayer ", x, "won the game! Get dunked on, losers!")
            winner = True
            break
        #x+=1

print("Game over")
    
    

