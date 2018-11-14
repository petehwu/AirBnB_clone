#!/usr/bin/python3
"""city unittest module"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.city import City

class TestCity(unittest.TestCase):
    """test case for City"""

    def setUp(self):
        """ sets up this each test """
        self.city = City()
        self.state_id = "98"
        self.name = "San Francisco"
        self.storage = FileStorage()

    def tearDown(self):
        """ tears down after each test. resets """
        del self.city

    def test_docstring(self):
        """ checks if docstring is there """
        self.assertIsNotNone(City.__doc__)

    def test_city_is_dict(self):
        """testing if dict"""
        st = FileStorage()
        st_dict = st.all()
        self.assertTrue(st_dict)
        self.assertEqual(dict, type(st_dict))

    def test_city(self):
        """ checks peter out. whatta hottie """
        self.assertTrue(self.city)
        self.assertEqual(self.name, "San Francisco")
        self.assertEqual(self.state_id, "98")

if __name__ == "__main__":
    unittest.main() 
