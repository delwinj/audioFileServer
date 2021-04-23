import unittest

from app import app
from database.db import db


class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

    def assert_response(self, response, expected_status_code, expected_content):
        status_code = response.status_code
        self.assertEqual(status_code, expected_status_code)
        self.assertEqual(response.content_type, "application/json")
        self.assertEqual(response.json, expected_content)

    def tearDown(self):
        # Delete Database collections after the test is complete
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
