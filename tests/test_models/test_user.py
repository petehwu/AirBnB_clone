#!/usr/bin/python3
"""User unittest module"""

import unittest
import os
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """test case for User"""

    def test_docstring(self):
        """ checks if docstring is there """
        self.assertIsNotNone(User.__doc__)

    def test_User_is_dict(self):
        """testing if dict"""
        st = FileStorage()
        st_dict = st.all()
        self.assertTrue(st_dict)
        self.assertEqual(dict, type(st_dict))

    def test_user(self):
        """testing user class"""
        u = User()
        self.assertIs(u, User)
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")
        self.assertNotEqual(u.id, "")
        u.email = "ppp@yahoo.com"
        u.first_name = "p"
        u.last_name = "w"
        u.password = "x"
        self.assertEqual(u.email, "ppp@yahoo.com")
        self.assertEqual(u.first_name, "p")
        self.assertEqual(u.last_name, "w")
        self.assertEqual(u.password, "x")

        

if __name__ == "__main__":
    unittest.main()
