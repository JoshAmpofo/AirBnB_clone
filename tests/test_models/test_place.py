#!/usr/bin/python3
"""Unittest cases for place.py"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test case suite for City module"""
    def setUp(self):
        """Sets up test methods"""
        self.place = Place()
        self.attr_list = ["user_id", "name", "city_id", "description",
                          "number_rooms", "number_bathrooms", "max_guest",
                          "price_by_night", "latitude", "longitude",
                          "amenity_ids"]

    def test_instantiations(self):
        """Check for city Place instances"""
        self.assertTrue(issubclass(type(self.place), BaseModel))
        for attr in self.attr_list:
            self.assertTrue(hasattr(Place, attr))

    def test_place_attributes(self):
        """Checks for place class attributes"""
        for attr in self.attr_list:
            self.assertFalse(bool(getattr(self.place, attr)))
        self.assertIs(type(self.place.name), str)
        self.assertIs(type(self.place.user_id), str)
        self.assertIs(type(self.place.city_id), str)
        self.assertIs(type(self.place.description), str)
        self.assertIs(type(self.place.number_rooms), int)
        self.assertIs(type(self.place.number_bathrooms), int)
        self.assertIs(type(self.place.max_guest), int)
        self.assertIs(type(self.place.price_by_night), int)
        self.assertIs(type(self.place.latitude), float)
        self.assertIs(type(self.place.longitude), float)
        self.assertIs(type(self.place.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
