import unittest
from unittest.mock import MagicMock
from db_handling_rod.db_handling_round_of_drinks import load_db, read_db, write_db, connect_to_db

class Test_handling_round_of_drinks(unittest.TestCase):    
    def test_person(self):
        # Arrange
        # people_list = []
        # drinks_list = []
        people_mock = MagicMock(wraps=people_list)
        drinks_mock = MagicMock(wraps=drinks_list)
        # Act
        people_list, drinks_list = load_db()
        # Assert
        people_mock.read_db.assert_called()

# class TestApp(unittest.TestCase):
#     def test_when_existing_person_submits_request_to_round_it_adds_preference(self):
#         # Arrange
#         round = Round(1, "John Doe")
#         requester = Person("Sally")
#         brewRequest = BrewRequest(requester)
#         expected = ["Capuccino"]
#         # Act
#         round.submit_request(brewRequest)
#         # Assert
#         requests = round.get_requests()
#         self.assertEqual(requests, expected)

    # def test_when_application_is_closed_app_data_is_saved_to_database(self):
    #     # Arrange
    #     db = Database()
    #     dbMock = MagicMock(wraps=db)
    #     app = app.App(db)
    #     # Act
    #     app.exit()
    #     # Assert
    #     dbMock.saveDrinks.assert_called()
    #     dbMock.savePeople.assert_called()
    #     dbMock.saveRounds.assert_called()

if __name__ == '__main__':
    unittest.main()