#!/usr/bin/python3
"""Unittest cases for review.py"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test case suite for Review module"""
    def setUp(self):
        """Sets up test methods"""
        self.review = Review()
        self.attr_list = ["user_id", "text", "place_id"]

    def test_instantiations(self):
        """Check for Review instances"""
        self.assertTrue(issubclass(type(self.review), BaseModel))
        for attr in self.attr_list:
            self.assertTrue(hasattr(self.review, attr))

    def test_review_attributes(self):
        """Checks for place class attributes"""
        for attr in self.attr_list:
            self.assertFalse(bool(getattr(self.review, attr)))
            self.assertIs(type(getattr(self.review, attr)), str)


if __name__ == '__main__':
    unittest.main()
