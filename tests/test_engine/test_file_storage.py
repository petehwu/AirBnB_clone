#!/usr/bin/python3
"""file_storage unittest module"""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """test cases for FileStorageclass"""

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
