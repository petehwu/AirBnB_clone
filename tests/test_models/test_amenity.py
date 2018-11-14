#!/usr/bin/python3
"""amenity unittest module"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test csae for amenity"""
    def setUp(self):
        """ sets up this each test """
        self.amenity = Amenity()
        self.amenity.name = "amenity"
        self.storage = FileStorage()

    def tearDown(self):
        """ tears down after each test. resets """
        del self.amenity

    def test_docstring(self):
        """ checks if docstring is there """
        self.assertIsNotNone(Amenity.__doc__)

    def test_file_storage_is_dict(self):
        """testing if dict"""
        st = FileStorage()
        st_dict = st.all()
        self.assertTrue(st_dict)
        self.assertEqual(dict, type(st_dict))

    def test_amenity(self):
        """ checks amenity """
        self.assertTrue(self.amenity)
        self.assertEqual(self.amenity.name, "amenity")

if __name__ == "__main__":
    unittest.main()
