#Imported modules for running the file
from unicodedata import name
from cryptography.fernet import Fernet #Modules allow to encrypt code


master_Key = input("Enter master password: ")#The master password that muct be remembered to do any functions

def make_Key():
        file = open("key.key", "rb")
        key = file.read()
        file.close() #Closes file as it is opened with "file ="
        return key

key = make_Key() + master_Key.bytes
fer = Fernet(key)



#Allows the user to view information on their encrypted file
def see_Credentials():
    with open('password_database.txt', 'r') as f: #With closes files when program ends, as oposed to file =, which requires a manual close. "w" over writes a files, "r" reads a file, "a" adds things to an existing file or creates one. 
            for line in f.readlines():
                data = line.rstrip() #gets rid of character return
                name, password, phoneNumber = data.split("|")
                print("Account Name:", name, "| Account Password:", fer.decrypt(password.encode()).decode(), "| Account Phone Number:", fer.decrypt(phoneNumber.encode()).decode())


#Allows the user to add information onto their encrypted file
def add_Credentials():
    name = input("Enter account name: ")
    password = input("Enter password: ")
    number = input("Enter phone number: ")
    
    with open('super_Secret_Password.txt', 'a') as f:
        f.write(name + "|" + str(fer.encrypt(password.encode()).decode()) + "|" + fer.encrypt(number.encode()).decode() + "\n")




#This will ask the user if they want to add or view information, then to input the master password, or simply quit
while True:
    userSelection = input("Do you want to view (1) password or add another password (2) (q to quit): ")
    userSelection.lower()
    if userSelection == "q":
        print("That's too bad. Have a nive day.")
        break

    elif userSelection == "v":
        while True:
                userInput = input("Enter the master password before viewing information: ")
                if userInput == master_Key:
                        break
                else:
                        print("Sorry that password is incorrect, try again or press q to quit")
                        continue
        view_info()
    elif userSelection == "a":
        while True:
                userInput = input("Enter the master password before adding information: ")
                if userInput == master_Key:
                        break
                elif userInput == "q":
                        quit()
                else:
                        print("Sorry that password is incorrect, try again or press q to quit")
                        continue
        add_info()
    else:
        print("Invalid input")
        continue
