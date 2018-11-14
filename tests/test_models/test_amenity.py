#!/usr/bin/python3
"""amenity unittest module"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test csae for amenity"""

    def test_docstring(self):
        """ checks if docstring is there """
        self.assertIsNotNone(Amenity.__doc__)

    def test_amenity(self):
        """ checks amenity """
        a = Amenity()
        self.assertEqual(type(a), Amenity)
        self.assertEqual(a.name, "")
        a.name = "b"
        self.assertEqual(a.name, "b")

if __name__ == "__main__":
    unittest.main()
