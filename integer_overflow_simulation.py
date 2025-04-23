def add(x, y):
    value = (x + y) % 2**8
    if value > 128:
        print("Gandhi is Unleashing the Nuclear Bomb!")
        return -(128 - (value//128))
    print("Gandhi is Satisfied!")
    return value

gandhi_value = 129

print(add(gandhi_value, 0))