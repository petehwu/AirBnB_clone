#!/usr/bin/python3
"""file_storage unittest module"""

import os
import json
import pep8
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

    def test_basic_init(self):
        """ tests the init and file path? """
        dank = BaseModel()
        poop = FileStorage()
        poopcopy = poop
        notpoop = FileStorage()
        self.assertEqual(poop, poopcopy)
        self.assertNotEqual(poop, notpoop)
        self.assertTrue(poop)
        self.assertFalse(poop == notpoop)
        self.assertIs(poop, poopcopy)
        self.assertIsNot(poop, notpoop)
        self.assertIsNotNone(poop)
        self.assertIsInstance(poop, FileStorage)
        self.assertNotIsInstance(dank, FileStorage)

    def test_google_doc(self):
        """ more harder tests """
        storage = FileStorage()
        # TEST ALL. NO CELL A
        # Cell B tests init and objects and file path
        self.assertEqual(type(storage._FileStorage__objects), dict)
        self.assertTrue(storage._FileStorage__objects)
        self.assertEqual(type(storage._FileStorage__file_path), str)
        self.assertEqual(storage._FileStorage__file_path, "file.json")

        # Cell C tests all() and type
        test = User()
        test2 = test.id
        key = "User." + test2
        all_storage = storage.all()
        self.assertEqual(type(all_storage), dict)
        self.assertEqual(str(type(
                all_storage[key])), "<class 'models.user.User'>")

        # Cell D tests new() and the dict
        my_model = BaseModel()
        self.assertEqual(
                str(type(my_model)), "<class 'models.base_model.BaseModel'>")
        self.assertEqual(
                sorted(my_model.__dict__.keys()),
                ['created_at', 'id', 'updated_at'])

        # Cell E tests save() and json file
        doesFileExist = User()
        self.assertTrue(os.path.isfile("file.json"))

        # Cell F tests reload and the json file
        os.rename("file.json", "CAKEisAlie")
        self.assertFalse(os.path.isfile("file.json"))
        newPoop = Place()
        self.assertTrue(storage._FileStorage__objects)
        os.rename("CAKEisAlie", "file.json")
        self.assertTrue(os.path.isfile("file.json"))

        # Cell G I stole this pep8 check online
        def test_pep8_conformance(self):
            """Test that we conform to PEP8."""
            pep8style = pep8.StyleGuide(quiet=True)
            result = pep8style.check_files(
                    ['tests/test_models/test_engine/test_file_storage.py',
                     'models/engine/file_storage.py'])
            self.assertEqual(
                    result.total_errors, 0,
                    "Found code style errors (and warnings).")
            # this doesnt work lol

if __name__ == "__main__":
    unittest.main()
