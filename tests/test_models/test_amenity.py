#!/usr/bin/python3
"""Unittest cases for amenity.py"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test case suite for Amenities module"""
    def setUp(self):
        """Sets up test methods"""
        self.amenity = Amenity()

    def test_instantiations(self):
        """Check for amenity class instances"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_amenity_attributes(self):
        """Checks for amenity class attributes"""
        self.assertIs(type(self.amenity.name), str)
        self.assertTrue(self.amenity.name == "")
        self.assertFalse(bool(getattr(self.amenity, "name")))


if __name__ == '__main__':
    unittest.main()
