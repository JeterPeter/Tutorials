


hashMap = {

    "1": "Garfield",
    "2": "Washington"

}

def keysToList(hashMap):
    #format a dict_keys object into a readable list
    keys = str(hashMap.keys())
    keys = keys.removeprefix("dict_keys([")
    keys = keys.removesuffix("])")
    keys = keys.replace("'", "")
    keys = keys.replace(",", "")
    keys = keys.split(" ")
    return keys










"""
print(thisdict)
thisdict.update({"color": "red"})
print(thisdict)
"""
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
    

