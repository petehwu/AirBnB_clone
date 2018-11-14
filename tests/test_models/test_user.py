#!/usr/bin/python3
"""User unittest module"""

import unittest
import os
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """test case for User"""
    def setUp(self):
        """ sets up this each test """
        self.user = User()
        self.user.id = "98"
        self.user.first_name = "Peter"
        self.user.last_name = "Wu"
        self.user.email = "naruto@hokage.com"
        self.storage = FileStorage()

    def tearDown(self):
        """ tears down after each test. resets """
        del self.user

    def test_docstring(self):
        """ checks if docstring is there """
        self.assertIsNotNone(FileStorage.__doc__)

    def test_file_storage_is_dict(self):
        """testing if dict"""
        st = FileStorage()
        st_dict = st.all()
        self.assertTrue(st_dict)
        self.assertEqual(dict, type(st_dict))

    def test_peter_wu(self):
        """ checks peter out. whatta hottie """
        self.assertTrue(self.user)
        self.assertEqual(self.user.first_name, "Peter")
        self.assertFalse(self.user.password)
        self.assertNotEqual(self.user.id, 98)
        self.assertEqual(self.user.id, "98")

if __name__ == "__main__":
    unittest.main()
