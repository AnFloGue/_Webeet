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
    """
    Test suite for the /characters endpoint.
    """

    def setUp(self):
        """
        Initializes the test client.
        """
        self.app = app.test_client()
        self.app.testing = True

    def get_characters(self, limit, skip):
        """
        Makes a GET request to /characters with limit and skip values.

        Args:
            limit (int): The number of characters to retrieve.
            skip (int): The number of characters to skip.

        Returns:
            Response: The response object from the GET request.
        """
        url = '/characters?limit=' + str(limit) + '&skip=' + str(skip)
        return self.app.get(url)

    def test_pagination_with_default_values(self):
        """
        Tests /characters with default limit and skip values.
        """
        response = self.get_characters(3, 0)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 3)

    def test_pagination_with_valid_values(self):
        """
        Tests /characters with valid limit and skip values.
        """
        response = self.get_characters(5, 10)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 5)

    def test_pagination_with_invalid_limit(self):
        """
        Tests /characters with an invalid limit value.
        """
        response = self.get_characters('invalid', 0)
        self.assertEqual(response.status_code, 400)

    def test_pagination_with_invalid_skip(self):
        """
        Tests /characters with an invalid skip value.
        """
        response = self.get_characters(3, 'invalid')
        self.assertEqual(response.status_code, 400)


class CharacterAPITestCase(unittest.TestCase):
    """
    Test suite for the /characters/<id> endpoint.
    """

    def setUp(self):
        """
        Initializes the test client.
        """
        self.app = app.test_client()
        self.app.testing = True

    def get_character_by_id_success(self):
        """
        Tests /characters/<id> with a valid ID.
        """
        response = self.app.get('/characters/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.get_json())

    def get_character_by_id_not_found(self):
        """
        Tests /characters/<id> with an invalid ID.
        """
        response = self.app.get('/characters/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {"error": "Character not found"})

if __name__ == "__main__":
    unittest.main()