#!/usr/bin/python3
"""Unittest cases for base_model.py
Unittest classes:
    TestBaseModel - line 16
"""

import os
import unittest
from datetime import datetime
from time import sleep
from uuid import uuid4
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for BaseModel class"""
    def test_id_instance(self):
        """test for instance id assignment on initialization"""
        bmd = BaseModel()
        self.assertTrue(hasattr(bmd, 'id'))
    def test_unique_id(self):
        """test if id instances are unique of each other"""
        bmd_1 = BaseModel()
        bmd_2 = BaseModel()
        self.assertNotEqual(bmd_1.id, bmd_2.id)
    def test_id_str(self):
        """check if id generated is a str"""
        bmd = BaseModel()
        self.assertTrue(type(bmd.id) is str)
    def test_created_at_datetime(self):
        """check if created_at is a datetime"""
        bmd = BaseModel()
        self.assertTrue(type(bmd.created_at) is datetime)
    def test_updated_at_datetime(self):
        """check if updated_at is a datetime"""
        bmd = BaseModel()
        self.assertTrue(type(bmd.updated_at) is datetime)
    def test_created_at_equal_updated_at_datetime(self):
        """check if initial datetime of created_at == datetime of updated at"""
        bmd = BaseModel()
        self.assertEqual(bmd.created_at, bmd.updated_at)
    def test_save(self):
        """check if update time is different from previous time"""
        bmd = BaseModel()
        sleep(0.05)
        bmd.save()
        self.assertNotEqual(bmd.updated_at, bmd.created_at)
        self.assertGreater(bmd.updated_at.microsecond,
                           bmd.created_at.microsecond)
    def test_str_format(self):
        """check if str rep is correct"""
        bmd = BaseModel()
        self.assertEqual(str(bmd), 
                "[BaseModel] ({}) {}".format(bmd.id, bmd.__dict__))
    def test_to_dict(self):
        """check if to_dict is dictionary"""
        bmd = BaseModel()
        self.assertTrue(type(bmd.to_dict()) is dict)
    def test_to_dict_class_dunder(self):
        """checks if BaseModel.to_dict() contains __class__"""
        bmd = BaseModel()
        self.assertTrue("__class__" in bmd.to_dict())
    def test_created_at_datetime_isoformat(self):
        """checks if datetime format of created_at is ISO"""
        bmd = BaseModel()
        self.assertEqual(bmd.to_dict()["created_at"], 
                bmd.created_at.isoformat())
    def test_updated_at_datetime_isoformat(self):
        """checks if datetime format of created_at is ISO"""
        bmd = BaseModel()
        self.assertEqual(bmd.to_dict()["updated_at"], 
                bmd.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()