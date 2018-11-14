#!/usr/bin/python3
"""review unittest module"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place
from models.review import Review


class TestReview(unittest.TestCase):
    """test cases for review class"""

    def setUp(self):
        """ sets up this each test """
        self.review = Review()
        self.review.place_id = "98"
        self.review.user_id = "Peter"
        self.review.text = "text"
        self.storage = FileStorage()

    def tearDown(self):
        """ tears down after each test. resets """
        del self.review

    def test_docstring(self):
        """ checks if docstring is there """
        self.assertIsNotNone(Review.__doc__)

    def test_file_storage_is_dict(self):
        """testing if dict"""
        st = FileStorage()
        st_dict = st.all()
        self.assertTrue(st_dict)
        self.assertEqual(dict, type(st_dict))

    def test_review(self):
        """ checks review out. whatta hottie """
        self.assertTrue(self.review)
        self.assertEqual(self.review.user_id, "Peter")
        self.assertNotEqual(self.review.place_id, 98)
        self.assertEqual(self.review.place_id, "98")
        self.assertEqual(self.review.text, "text")

if __name__ == "__main__":
    unittest.main()
