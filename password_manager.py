from cryptography.fernet import Fernet
 
'''
def write_key() :
    key = Fernet.generate_key()           
    with open("key.key", "wb") as key_file : # wb -> write in bytes
        key_file.write(key)
'''

def load_key() :
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
 # first the function should be created then it can be read. inpreter things
key = load_key() # first the function should be created then it can be read. inpreter things
fer = Fernet(key)

def view() :
    with open('passwords.txt', "r") as f : # with open automatically close the file, so bteer than open() -> r : read , w : write,  a : append
        for line in f.readlines() : # readlines() reads all the lines from the file
            data = line.rstrip() # in my case the rstrip remove the carriage return or line added after the password
            
            user,pwd = data.split("|")
            print("Username :",user)
            print("Password :",fer.decrypt(pwd.encode()).decode())


def add() :
    name = input("Please provide the username : ")
    pwd = input("Please provide the password : ")

    with open('passwords.txt', 'a') as f :
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    user_choice = input("Would you like to add a new passowrd or view an existing one? (view, add, quit) :").lower()

    if user_choice == 'quit' :
        break

    if user_choice == "add" :
        add()
    else :
        view()