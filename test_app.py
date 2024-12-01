# test_app.py
import unittest
from app import app

"""
This test suite contains tests for the /characters and /characters/<id> endpoints.

TestGetCharacters:
- setUp: Initializes the test client.
- get_characters: Makes a GET request to /characters with limit and skip values.
- test_pagination_with_default_values: Tests /characters with default limit and skip.
- test_pagination_with_valid_values: Tests /characters with valid limit and skip.
- test_pagination_with_invalid_limit: Tests /characters with an invalid limit.
- test_pagination_with_invalid_skip: Tests /characters with an invalid skip.

CharacterAPITestCase:
- setUp: Initializes the test client.
- get_character_by_id_success: Tests /characters/<id> with a valid ID.
- get_character_by_id_not_found: Tests /characters/<id> with an invalid ID.

The tests use assertEqual and assertIn to verify the response status and data.
Run the tests with unittest.main().
"""

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

