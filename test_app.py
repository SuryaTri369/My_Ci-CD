import unittest
from app import app, items  # Import `items` so we can modify it in tests

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        # Reset the `items` list to its original state before each test
        items.clear()
        items.extend([
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
        ])
        self.app = app.test_client()
        self.app.testing = True

    def test_get_items(self):
        response = self.app.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)  # Initially, we have 2 items

    def test_add_item(self):
        new_item = {"id": 3, "name": "Item 3"}
        response = self.app.post('/items', json=new_item)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, new_item)

        # Verify that the item was added
        response = self.app.get('/items')
        self.assertEqual(len(response.json), 3)  # Now we should have 3 items

if __name__ == '__main__':
    unittest.main()
