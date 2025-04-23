import json

def get_new_favorite():  
    with open("favorite_number.json", "w") as fav:
        fav_num = input("What is your favorite number: ")
        json.dump(fav_num, fav)
        return fav_num

def get_user_favorite():
    try:
        with open("favorite_number.json", "r") as fav:
            fav_num = json.load(fav)
    except FileNotFoundError:
        return None
    return fav_num

def greet_user():
    favorite_number = get_user_favorite()
    if favorite_number:
        print(f"Your Favorite Number is {favorite_number}")
    else:
        new_favorite = get_new_favorite()
        print(f"We'll remember your favorite number is {new_favorite}")

greet_user()