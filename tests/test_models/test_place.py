#!/usr/bin/python3
"""place unittest module"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.place import Place

class TestPlace(unittest.TestCase):
    """test case for Place"""

    def test_docstring(self):
        """ checks if docstring is there """
        self.assertIsNotNone(Place.__doc__)

    def test_Place(self):
        """ checks Place class """
        p = Place()
        self.assertEqual(type(p), Place)
        self.assertEqual(p.city_id, "")
        self.assertEqual(p.user_id, "")
        self.assertEqual(p.name, "")
        self.assertEqual(p.description, "")
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.price_by_night, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)
        self.assertEqual(p.amenity_ids, [])

        p.city_id = "a"
        p.user_id = "b"
        p.name = "c"
        p.description = "d"
        p.number_rooms = 1
        p.number_bathrooms = 2
        p.max_guest = 3
        p.price_by_night = 4
        p.latitude = 1.1
        p.longitude = 2.2
        p.amenity_ids = [1,2]

        self.assertEqual(p.city_id, "a")
        self.assertEqual(p.user_id, "b")
        self.assertEqual(p.name, "c")
        self.assertEqual(p.description, "d")
        self.assertEqual(p.number_rooms, 1)
        self.assertEqual(p.number_bathrooms, 2)
        self.assertEqual(p.max_guest, 3)
        self.assertEqual(p.price_by_night, 4)
        self.assertEqual(p.latitude, 1.1)
        self.assertEqual(p.longitude, 2.2)
        self.assertListEqual(p.amenity_ids, [1,2])

if __name__ == "__main__":
    unittest.main()
