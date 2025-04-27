import unittest
from city_functions import formatted_location


class City(unittest.TestCase):

    def setUp(self):
        self.city, self.country = "lipa city", "philippines"
        self.city, self.country, self.pop = "lipa city", "philippines", 100092

    def test_city_country(self):
        test_case = formatted_location(self.city, self.country)
        if self.city == "lipa city":
            self.assertEqual(test_case, "Philippines, Lipa City")
        else:
            self.assertEqual(test_case, "Usa, New York")
    
    def test_city_country_pop(self):
        test_case = formatted_location(self.city, self.country, self.pop)
        print(test_case)

        self.assertEqual(test_case, "Philippines, Lipa City: 100092")
 

if __name__ == '__main__':
    unittest.main()



