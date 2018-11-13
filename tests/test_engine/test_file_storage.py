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

    def test_file_storage(self):
        """testing the BaseModel"""
        st = FileStorage()
        st.reload()
