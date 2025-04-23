class Arithmetic():
    def __init__(self, x, y):
        self.num1 = x
        self.__num2 = y
    def add(self):
        return self.num1 + self.__num2
    def multiply(self):
        return self.num1 * self.__num2
    def divide(self):
        return self.num1 * self.__num2
    def subtract(self):
        return self.num1 * self.__num2
    
class Hidden(Arithmetic):
    def __init__(self, x, y):
        super().__init__(x ,y)
        
    def __add(self):
        return super().add()

    def test_add(self):
        return self.__add()
    
# class Arithmetic2(Arithmetic):


var = Arithmetic(5, 6)
var2 = Hidden(10, 9)
print(var.num1, "S1")
# print(var.__num2, "S2")
# print(var.add())
# print(var2.add())
print(var2.test_add())
