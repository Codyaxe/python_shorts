import time

def distance(x: tuple, y: tuple):
    coordinates = ((y[0]-x[0])**2, (y[1]- x[1])**2)
    return int((coordinates[0] + coordinates[1])**(0.5))

def input_to_coords(x: str): 
    new_list = list(map(int, x.replace("(", "").replace(")", "").split(",")))
    a = (new_list[0], new_list[1])
    b = (new_list[2], new_list[3])
    return a,b
    

try:
    coords1, coords2 = input_to_coords(input("Insert Two Coordinates Using Parenthesis: "))
    time.sleep(0.5)
    print(coords1, coords2)
    time.sleep(2)
    print(f"The distance between the two coordinates is: {distance(coords1, coords2)}")
except TypeError as e:
    print(f"Invalid Input: {e}")

