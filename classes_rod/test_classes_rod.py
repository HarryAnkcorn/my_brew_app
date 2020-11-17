import unittest

from classes_rod.classes_round_of_drinks import Person, Drink, Order

class Test_classes_round_of_drinks(unittest.TestCase):
    
    def test_person(self):
        test_person = Person("", 'dave', 'test', 53, 'Human')

        expected_person_first_name = 'dave'
        expected_person_last_name = 'test'
        expected_person_age = 53
        expected_person_race = 'Human'

        self.assertEqual(test_person.first_name, expected_person_first_name)
        self.assertEqual(test_person.last_name, expected_person_last_name)
        self.assertEqual(test_person.age, expected_person_age)
        self.assertEqual(test_person.race, expected_person_race)
    
    def test_Drink(self):
        test_drink = Drink("", 'coke', 100, 'yes')

        expected_drink_name = 'coke'
        expected_drink_price = 100
        expected_drink_is_mixer = 'yes'

        self.assertEqual(test_drink.name, expected_drink_name)
        self.assertEqual(test_drink.price, expected_drink_price)
        self.assertEqual(test_drink.is_mixer, expected_drink_is_mixer)

    def test_Order(self):
        test_order = Order("", 'Frodo', "['Frodo', 'gin', 'Samewise', 'gin']", 10.00)
        expected_person = 'Frodo'
        expected_person_drink = "['Frodo', 'gin', 'Samewise', 'gin']"
        expected_cost = 10.00

        self.assertEqual(test_order.person, expected_person)
        self.assertEqual(test_order.people_drinks, expected_person_drink)
        self.assertEqual(test_order.cost, expected_cost)

if __name__ == '__main__':
    unittest.main()