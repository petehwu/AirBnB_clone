#!/usr/bin/python3
"""base_model unittest module"""

import os
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """test cases for BaseModel class"""

    def test_base_model(self):
        """testing the BaseModel"""
        bm = BaseModel()
        self.assertIs(type(bm.id), str)
        self.assertIs(type(bm.created_at), datetime)
        self.assertIs(type(bm.updated_at), datetime)
        old_updated = bm.updated_at
        bm.save()
        self.assertNotEqual(old_updated, bm.updated_at)
