#!/usr/bin/python3
"""base_model unittest module"""

import os
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class TestBaseModel(unittest.TestCase):
    """test cases for BaseModel class"""

    def test_base_model(self):
        """testing the BaseModel"""
        bm = BaseModel()
        self.assertIs(type(bm.id), str)
        self.assertIs(type(bm.created_at), datetime)
        self.assertIs(type(bm.updated_at), datetime)
        self.assertNotEqual(bm.created_at, bm.updated_at)
        self.assertFalse(bm.updated_at == datetime.utcnow())
        old_updated = bm.updated_at
        bm.save()
        self.assertNotEqual(old_updated, bm.updated_at)
        d = bm.to_dict()
        self.assertEqual(type(d), dict)
        self.assertEqual(d['__class__'], "BaseModel")
        self.assertEqual(d['created_at'], bm.created_at.isoformat())
        self.assertEqual(d['updated_at'], bm.updated_at.isoformat())
        self.assertEqual(d['id'], bm.id)

    def test_init_with_dict(self):
        """testing init method"""
        dd = {"id": "123-123-123",
              "key1": "val1", "key2": "val2", "key3": "val3"}
        b = BaseModel(**dd)
        self.assertEqual(b.id, "123-123-123")
        self.assertEqual(b.key1, "val1")
        self.assertEqual(b.key2, "val2")
        self.assertEqual(b.key3, "val3")

if __name__ == '__main__':
    unittest.main()
