def deco_function(function):
    var = "a"
    def inner_function(dec):
        print(var)
        function()
        return dec()
    return inner_function

def deco_function2(function):
    number = 1
    def inner_function():
        print(number, "S1")
        print(value, "S2")
        return function()
    value = 3
    return inner_function

@deco_function
def message_endslash():
    print("Test1 ", end= "\\")
def lol():
    print("Hi")
message_endslash(lol)

def message_endcomma():
    print("Test2", end=",")
message1 = deco_function2(message_endcomma)
message1()
