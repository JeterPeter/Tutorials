"""
This particular draft of pig failed because I couldn't figure out how to use the keyboard listener correctly. 
It would not run the listener in the background while other things were running, causing it to be stuck listening and not having a final output.
I think the main problem revolved around the input() function. Without it, the listener wouldn't detect anything unless in a loop - but would then output the same thing infinitely.
If input() was included, it would receive inputs but would not be able to break from it, not even with a return False to stop the listener.
The solution was to create the listener in a different way, like this:

with Listener(on_press=pressed) as listener:
        listener.join()
    
It was not required to be in a loop when like this.
"""





#this is the module to hold functions for the pig game
import random
from pynput import keyboard



def rollDie():
    #return random number 1-6
    return random.randrange(2,7)

#runs a player's turn
def turn():
    
    global score
    global stop
    global rolls
    score = 0
    stop = False
    rolls = 0

    def spacePress(key):
        #while stop == False:
            print("The while loop in spacePress has looped!")
            print("spacePress is going")
            global score
            global stop
            global rolls
            if key == keyboard.Key.space:
                cast = rollDie()
                print("You rolled a ", cast, "!")
                if cast == 1:
                    score = 0
                    stop = True
                    print("Your turn has ended because you rolled a 1! Press escape to continue.") 
                    #return False             
                else:
                    score = score + cast
                    rolls+=1
                    print("You have rolled ", rolls, " times. Press escape to roll again or enter to finish your turn!")
                    #return False
            if key == keyboard.Key.esc:                
                return False
        

        

    #begin turn code
    listener = keyboard.Listener(on_release=spacePress)
    listener.start()
    input()
    
    print("Press space to roll the die. Press escape to end your turn.")
    while stop == False:
        #print("While loop has looped")
        pass
   
    #listener.stop()
    print("Your final score for this turn is :", score)
    return score