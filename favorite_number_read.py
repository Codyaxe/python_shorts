import json

with open("favorite_number.json", "r") as fav:
    print(f"I know your favorite number! It’s {json.load(fav)}")
    