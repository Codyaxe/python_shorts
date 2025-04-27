import unittest

class Employee():

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    
    def give_raise(self, amount = 5000):
        self.salary += amount
    

class TestEmployee(unittest.TestCase):

    def setUp(self):

        self.employee_1 = Employee("Juan","Cruz", 0)
        self.employee_2 = Employee("Sean", "Ace", 0)
        self.employee_3 = Employee("Sebastian", "Martini", 0)
        self.employees = [self.employee_1, self.employee_2, self.employee_3]

    
    def test_give_default_raise(self):
        for i in self.employees:
            expected = f"{i.first} {i.last}: 5000"
            i.give_raise()
            self.assertEqual(f"{i.first} {i.last}: {i.salary}", expected)

    def test_give_custom_raise(self):
        amount = 6000
        for i in self.employees:
            expected = f"{i.first} {i.last}: {amount}"
            i.give_raise(amount)
            self.assertEqual(f"{i.first} {i.last}: {i.salary}", expected)



if __name__ ==  "__main__":
    unittest.main()