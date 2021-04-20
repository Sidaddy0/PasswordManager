# Password Manager
from json import dump, load
from random import sample
from string import printable

from pybase64 import b64decode, b64encode

encrypt = lambda x: b64encode(bytes(str(x), "ascii"))
decrypt = lambda x: b64decode(bytes(str(x), "ascii"), validate = True)

everything = printable[0:90]

def search(type_of_search: int):
    if type_of_search == 1:
        while True:
            try:
                return decrypt(website_search[input("Enter website name: ")])
            except Exception as e:
                print(e)
    elif type_of_search == 2:
        while True:
            try:
                return decrypt(username_search[input("Enter username: ")])
            except Exception as e:
                print(e)

def store_password(website: str, username: str):
    # Enter a password or generate a random password
    while True:
        try:
            x = int(input("Type 1 if you want to store your own password and type 2 if you want to generate a password for the website. "))
            break
        except Exception as e:
            print(e)
    
    if x == 1:
        password = input("Password: ")
    elif x == 2:
        length = int(input("Length of password: "))
        password = "".join(sample(everything, length))
    # Hash the password
    password = encrypt(password)
    # Store the password
    username_search[username] = password
    website_search[website] = password

if __name__ == "__main__":
    # HashMaps
    with open("username_search.json", "r") as f:
        username_search = load(f)
    with open("website_search.json", "r") as f:
        website_search = load(f)

    search_type = int(input("Type 1 to search by website, 2 to search by username, and 3 to store a new password. "))
    if search_type == 1:
        print(search(1))
    elif search_type == 2:
        print(search(2))
    elif search_type == 3:
        store_password(input("Enter website name: "), input("Enter username: "))
        with open("username_search.json", "w") as f:
            dump(dict(username_search), f)
        with open("website_search.json", "w") as f:
            dump(dict(website_search), f)
        print("Successfully stored password.")
