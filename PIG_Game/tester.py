from pynput import keyboard
import pig

print(pig.turn())


"""
def keyPressed(key):
    print(str(key))

listener = keyboard.Listener(on_press=keyPressed)
listener.start()                 
input()


def onPress(key):
    if key == keyboard.Key.space:
        print("bang")
    if key == keyboard.Key.esc:
        return False 
    
    with keyboard.Listener(on_press=onPress) as listener:  listener.join()
    """
                   

