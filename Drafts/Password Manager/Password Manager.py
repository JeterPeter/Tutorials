from cryptography.fernet import Fernet

def loadKey():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("what is the master password? ")
key = loadKey() + master_pwd.encode()
fer = Fernet(key)


"""
def writeKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as keyFile:
        keyFile.write(key)
writeKey()
"""


def view():
    print("Your saved usernames and passwords:\n")
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data =line.rstrip()
            user,password = data.split(" | ")
            print("User: ",user, "\nPassword: ", str(fer.decrypt(password.encode())), "\n")

def add():
    name = input("Account Name: ")
    password = input("Password: ")
    
    with open('passwords.txt', "a") as f:
        f.write(name + " | " + str(fer.encrypt(password.encode())) + "\n")



mode = input("Would you like to add a new password or view existing passwords? (type view or add)\nType \"q\" to quit\n").lower()
#mode = mode.lower()

if mode == "q":
    quit()

if mode == "view":
    view()
elif mode == 'add':
    add()
else:
    print("invalid mode")