import math as m

def square_roots(numbers: list):
    return [m.sqrt(number) for number in numbers]
    

square_list = square_roots([x for x in range(10)])
print(square_list)
