#!/usr/bin/python3
"""State unittest module"""

import unittest
import os
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """test case for State"""

    def setUp(self):
        """ sets up this each test """
        self.state = State()
        self.state.name = "California"
        self.storage = FileStorage()

    def tearDown(self):
        """ tears down after each test. resets """
        del self.state

    def test_docstring(self):
        """ checks if docstring is there """
        self.assertIsNotNone(State.__doc__)

    def test_file_storage_is_dict(self):
        """testing if dict"""
        st = FileStorage()
        st_dict = st.all()
        self.assertTrue(st_dict)
        self.assertEqual(dict, type(st_dict))

    def test_california(self):
        """ checks california out. whatta hottie """
        self.assertTrue(self.state)
        self.assertEqual(self.state.name, "California")

if __name__ == "__main__":
    unittest.main()
