import json
import os

USER_FILE = "data/users.json"

def load_users():

    if not os.path.exists(USER_FILE):
        return {}

    with open(USER_FILE) as f:
        return json.load(f)

def save_users(users):

    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

def login_or_signup():

    users = load_users()

    while True:

        choice = input("Login or Signup (l/s): ").lower()

        if choice == "l":

            username = input("Username: ")
            password = input("Password: ")

            if username in users and users[username] == password:
                print("Login successful")
                return username
            else:
                print("Invalid login")

        elif choice == "s":

            username = input("Choose username: ")
            password = input("Choose password: ")

            if username in users:
                print("Username already exists")
            else:
                users[username] = password
                save_users(users)
                print("Account created")
