# test_app.py
import unittest
from app import app

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

if __name__ == '__main__':
    unittest.main()