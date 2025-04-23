import json

def greet_user():
    try:
        with open("username.json", "r") as user:
            username = json.load(user)
            choice = input(f"Are you {username}? Press Y or N: ").lower()
            if choice == "y":
                print(f"Welcome Back {username}!")
            elif choice == "n":
                new_user = get_new_user()
                print(f"New user established! Hello {new_user}!")
    except FileNotFoundError:
        print("User not found!")
        new_user = get_new_user()
        print(f"We'll remember you {new_user}!")
    
def get_new_user():
    with open("username.json", "w") as user:
        new_user = input("Who are you? ")
        json.dump(new_user, user)
        return new_user

greet_user()