#!/usr/bin/python3
"""Unittest cases for user.py
Unittest classes:
    TestUser - line 18
"""

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestUser(unittest.TestCase):
    """Test case suite for User module"""
    def setUp(self):
        """Sets up test methods"""
        pass

    def tearDown(self):
        """cleans up test methods created by Setup"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiations(self):
        """Check for correct user class instances"""
        bmd = User()
        self.assertEqual(str(type(bmd)), "<class 'models.user.User'>")
        self.assertIsInstance(bmd, User)
        self.assertTrue(issubclass(type(bmd), BaseModel))

    def test_user_attributes(self):
        """Checks for user attributes"""
        user = User()
        self.assertIs(type(user.first_name), str)
        self.assertIs(type(user.last_name), str)
        self.assertTrue(user.first_name == "")
        self.assertTrue(user.last_name == "")


if __name__ == '__main__':
    unittest.main()
