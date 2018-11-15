#!/usr/bin/python3
"""place unittest module"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.place import Place


class TestPlace(unittest.TestCase):
    """test case for Place"""

    def setUp(self):
        """ sets up this each test """
        self.place = Place()
        self.place.city_id = "100-100"
        self.place.user_id = "101-101"
        self.place.name = "place_name"
        self.place.description = "place_description"
        self.place.number_rooms = 5
        self.place.number_bathrooms = 5
        self.place.max_guest = 5
        self.place.price_by_night = 5
        self.place.latitude = 10.0
        self.place.longitude = 10.0
        self.place.amenity_ids = ["1-1-1", "2-2-2"]
        self.storage = FileStorage()

    def tearDown(self):
        """ tears down after each test. resets """
        del self.place

    def test_docstring(self):
        """ checks if docstring is there """
        self.assertIsNotNone(Place.__doc__)

    def test_Place_is_dict(self):
        """testing if dict"""
        st = FileStorage()
        st_dict = st.all()
        self.assertTrue(st_dict)
        self.assertEqual(dict, type(st_dict))

    def test_Place(self):
        """ checks Place  out. whatta hottie """
        self.assertTrue(self.place)
        self.assertEqual(self.place.city_id, "100-100")
        self.assertEqual(self.place.user_id, "101-101")
        self.assertEqual(self.place.name, "place_name")
        self.assertEqual(self.place.description, "place_description")
        self.assertEqual(self.place.number_rooms, 5)
        self.assertIs(type(self.place.number_rooms), int)
        self.assertEqual(self.place.number_bathrooms, 5)
        self.assertIs(type(self.place.number_bathrooms), int)
        self.assertEqual(self.place.max_guest, 5)
        self.assertIs(type(self.place.max_guest), int)
        self.assertEqual(self.place.price_by_night, 5)
        self.assertIs(type(self.place.price_by_night), int)
        self.assertEqual(self.place.latitude, 10.0)
        self.assertIs(type(self.place.latitude), float)
        self.assertEqual(self.place.longitude, 10.0)
        self.assertIs(type(self.place.longitude), float)
        self.assertListEqual(self.place.amenity_ids, ["1-1-1", "2-2-2"])


if __name__ == "__main__":
    unittest.main()
