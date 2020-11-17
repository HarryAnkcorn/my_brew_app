import unittest
from unittest.mock import patch

from logic_rod.logic_round_of_drinks import get_input, add_person, add_drink, edit_arg, order_drinks
from classes_rod.classes_round_of_drinks import Person, Drink, Order

class Test_logic(unittest.TestCase):

    @patch('logic_rod.logic_round_of_drinks.get_input', side_effect = ['Frodo', 'Baggins', 50, '3'])
    def test_add_person(self, input):
        lst = []
        answer = "[Frodo, Baggins, 50, gin]"
        drinks_list = []
        drinks_list.append(Drink("", 'Beer', 3.2, 'no'))
        drinks_list.append(Drink("", 'cider', 3.5, 'no'))
        drinks_list.append(Drink("", 'gin', 5.0, 'no'))

        self.assertEqual(str(add_person(lst, drinks_list)), answer)

    @patch('logic_rod.logic_round_of_drinks.get_input', side_effect = ['Beer', 3, 'No'])
    def test_add_drink(self, input):
        lst = []
        answer = "[Beer, £3.00, No]"
        self.assertEqual(str(add_drink(lst)), answer)

    @patch('logic_rod.logic_round_of_drinks.get_input', side_effect = ['1', '1','Frodo'])
    def test_edit_person_name(self, input):
        lst = []
        lst.append(Person("",'Frodope', 'Baggins', 50, 'beer'))
        lst.append(Person("", 'Samewise', 'Gamgee', 38,'beer'))
        answer = "[Frodo, Baggins, 50, beer, Samewise, Gamgee, 38, beer]"
        self.assertEqual(str(edit_arg("person",lst, None)), answer)

    @patch('logic_rod.logic_round_of_drinks.get_input', side_effect = ['2', '5'])
    def test_delete_person(self, input):
        lst = []
        lst.append(Person("",'Frodo', 'Baggins', 50, 'beer'))
        lst.append(Person("", 'Samewise', 'Gamgee', 38,'beer'))
        answer = "[Frodo, Baggins, 50, beer]"
        self.assertEqual(str(edit_arg("person",lst, None)), answer)

    @patch('logic_rod.logic_round_of_drinks.get_input', side_effect = ['2', '2', 19.99])
    def test_edit_drink_price(self, input):
        lst = []
        lst.append(Drink("", 'Beer', 3.2, 'no'))
        lst.append(Drink("", 'cider', 3.5, 'no'))
        answer = "[Beer, £3.20, no, cider, £19.99, no]"
        self.assertEqual(str(edit_arg("drink",lst, None)), answer)

    @patch('logic_rod.logic_round_of_drinks.get_input', side_effect = ['1', '4'])
    def test_delete_drink(self, input):
        lst = []
        lst.append(Drink("",'Beer', 3.2, 'no'))
        lst.append(Drink("", 'cider', 3.5, 'no'))
        answer = "[cider, £3.50, no]"
        self.assertEqual(str(edit_arg("drink",lst, None)), answer)

    @patch('logic_rod.logic_round_of_drinks.get_input', side_effect = ['1', '1', '4'])
    def test_order_drinks(self, input):
        people_list = []
        people_list.append(Person("",'Frodo', 'Baggins', 50, 'gin'))
        people_list.append(Person("", 'Samewise', 'Gamgee', 38, 'beer'))

        drinks_list = []
        drinks_list.append(Drink("", 'Beer', 3.2, 'no'))
        drinks_list.append(Drink("", 'cider', 3.5, 'no'))
        drinks_list.append(Drink("", 'gin', 5.0, 'no'))

        past_orders = []

        answer = "Frodo, ['Frodo', 'gin', 'Samewise', 'gin'], £10.00"
        self.assertEqual(str(order_drinks(people_list, drinks_list, past_orders, is_test = True)), answer)

if __name__ == '__main__':
    unittest.main()