#this is the module to hold functions for the pig game
import random
from pynput import keyboard
from pynput.keyboard import Key, Listener



def rollDie():
    #return random number 1-6
    return random.randrange(1,7)

#runs a player's turn 
def turn():
    
    global score
    global stop
    global rolls
    score = 0
    stop = False
    rolls = 0

    print("Press space to roll the die or enter to end your turn! Roll as many times as you like, but remember that if you roll a 1 you can lose it all!")
    
    def pressed(key): 

        global stop
        global score
        global rolls

        if key == keyboard.Key.space:
            cast = rollDie()
            print("You rolled a ", cast, "!")
            if cast == 1:
                score = 0
                #stop = True
                print("Your turn has ended because you rolled a 1! Press escape to continue.") 
                return False             
            else:
                score = score + cast
                rolls+=1
                print("You have rolled ", rolls, " times. Press escape to roll again or enter to finish your turn!")
                #return False

        if key == keyboard.Key.enter:
            return False
            

    with Listener(on_press=pressed) as listener:
        listener.join()
    #print("listener stopped, the score is ", score)
    return score


