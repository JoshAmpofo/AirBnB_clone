#!/usr/bin/python3
"""Unittest cases for city.py"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test case suite for City module"""
    def setUp(self):
        """Sets up test methods"""
        self.city = City()
        self.attr_list = ["state_id", "name"]

    def test_instantiations(self):
        """Check for city class instances"""
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_city_attributes(self):
        """Checks for city class attributes"""
        for attr in self.attr_list:
            self.assertIs(type(getattr(self.city, attr)), str)
            self.assertFalse(bool(getattr(self.city, attr)))


if __name__ == '__main__':
    unittest.main()
