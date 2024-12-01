# test_app.py
import unittest
from app import app


# In this test, we have two test cases. The first one tests the get_characters endpoint with default values for limit and skip. The second test case tests the get_characters endpoint with valid values for limit and skip. The third test case tests the get_characters endpoint with an invalid limit value. The fourth test case tests the get_characters endpoint with an invalid skip value. The setUp method is used to set up the test client and set the testing flag to True. The get_characters method is used to make a GET request to the /characters endpoint with the specified limit and skip values. The test_pagination_with_default_values method tests the get_characters endpoint with default values for limit and skip. The test_pagination_with_valid_values method tests the get_characters endpoint with valid values for limit and skip. The test_pagination_with_invalid_limit method tests the get_characters endpoint with an invalid limit value. The test_pagination_with_invalid_skip method tests the get_characters endpoint with an invalid skip value. The CharacterAPITestCase class contains two test methods: get_character_by_id_success and get_character_by_id_not_found. The get_character_by_id_success method tests the get_character_by_id endpoint with a valid character ID. The get_character_by_id_not_found method tests the get_character_by_id endpoint with an invalid character ID. The test cases use the assertEqual and assertIn methods to check the response status code and the response JSON data. The test cases also use the assertEqual method to check the response JSON data against the expected values. The unittest.main() method is used to run the test cases. When you run the test_app.py file, you should see the test results displayed in the console. If all the test cases pass, you should see the message "OK" at the end of the output. If any test case fails, you should see an error message indicating the reason for the failure.
class TestGetCharacters(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def get_characters(self, limit, skip):
        url = '/characters?limit=' + str(limit) + '&skip=' + str(skip)
        return self.app.get(url)

    def test_pagination_with_default_values(self):
        response = self.get_characters(3, 0)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 3)

    def test_pagination_with_valid_values(self):
        response = self.get_characters(5, 10)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 5)

    def test_pagination_with_invalid_limit(self):
        response = self.get_characters('invalid', 0)
        self.assertEqual(response.status_code, 400)

    def test_pagination_with_invalid_skip(self):
        response = self.get_characters(3, 'invalid')
        self.assertEqual(response.status_code, 400)
        
        


class CharacterAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def get_character_by_id_success(self):
        response = self.app.get('/characters/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.get_json())

    def get_character_by_id_not_found(self):
        response = self.app.get('/characters/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {"error": "Character not found"})

if __name__ == "__main__":
    unittest.main()

