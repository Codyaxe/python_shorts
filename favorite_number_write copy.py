import json

with open("favorite_number.json", "w") as fav:
    fav_num = input("What is your favorite number: ")
    json.dump(fav_num, fav)