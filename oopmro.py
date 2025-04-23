from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def rk(self):
        pass

class B(A):
    def rk(self):
        print("In class B")
        
    def do_something(self):
        print("I did something!")

class C(A):
    def rk(self):
        print("In class C")

class D(C, B):
    pass

r = B()
r.rk()
r.do_something()

try:
    r = A()

except TypeError as e:
    print(f"Abstract Base Class Instantiation: {e}")