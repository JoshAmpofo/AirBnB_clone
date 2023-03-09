#!/usr/bin/python3
"""Unittest cases for state.py"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test case suite for Review module"""
    def setUp(self):
        """Sets up test methods"""
        self.state = State()

    def test_instantiations(self):
        """Check for State instances"""
        self.assertTrue(issubclass(type(self.state), BaseModel))
        self.assertTrue(hasattr(self.state, "name"))

    def test_state_attributes(self):
        """Checks for state class attributes"""
        self.assertFalse(bool(self.state.name))
        self.assertIs(type(self.state.name), str)


if __name__ == '__main__':
    unittest.main()
