class A():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_age(self):
        return self.__age
    
    @get_age.setter
    def change_age(self, new_age):
        self.__age = new_age + 1


v = A(name = "Rawr", age = 18)
print(v.get_age)
v.change_age = 20
print(v.get_age)
v.get_name

