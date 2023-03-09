#!/usr/bin/python3
"""Unittest cases for base_model.py"""

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

    def test_no_args_usage(self):
        """checks if *args is not used in BaseModel dictionary"""
        bmd = BaseModel(None)
        self.assertNotIn(None, bmd.__dict__.values())

    def test_diff_created_at_of_models(self):
        """checks if two created_at instances differ"""
        bmd_1 = BaseModel()
        sleep(0.05)
        bmd_2 = BaseModel()
        sleep(0.05)
        self.assertLess(bmd_1.created_at, bmd_2.created_at)

    def test_kwargs_not_empty(self):
        """checks if id, created_at and updated_at are created from kwargs"""
        obj_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                    "updated_at": datetime.utcnow().isoformat()}
        bmd = BaseModel(**obj_dict)
        self.assertEqual(bmd.id, obj_dict["id"])
        self.assertEqual(bmd.created_at,
                         datetime.strptime(obj_dict["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))

    def test_kwargs_empty(self):
        """checks if id, created_at and update_at are generated
           automatically if not in kwargs
        """
        obj_dict = {}
        bmd = BaseModel(**obj_dict)
        self.assertTrue(type(bmd.id) is str)
        self.assertTrue(type(bmd.created_at) is datetime)
        self.assertTrue(type(bmd.updated_at) is datetime)

    def test_kwargs_passed(self):
        """Checks for kwargs and ignores args in BaseModel instance"""
        obj_dt = datetime.now()
        obj_dt_iso = obj_dt.isoformat()
        bmd = BaseModel("1234", id="599", created_at=obj_dt_iso, name="AirBnB")
        self.assertEqual(bmd.id, "599")
        self.assertEqual(bmd.created_at, obj_dt)
        self.assertEqual(bmd.name, "AirBnB")

    def test_dict_obj_to_BaseModel(self):
        """checks if storage.new() is not called when a BaseModel obj is
           created from a dict obj
        """
        obj_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                    "updated_at": datetime.utcnow().isoformat(),
                    "name": "AirBnB"}
        bmd = BaseModel(**obj_dict)
        self.assertNotIn(bmd, models.storage.all().values())

        del bmd

        bmd = BaseModel()
        self.assertIn(bmd, models.storage.all().values())

    def test_save_update_updated_at(self):
        """Checks if the save() method updates "updated_at" attr"""
        bmd = BaseModel()
        sleep(0.05)
        temp_update = bmd.updated_at
        bmd.save()
        self.assertLess(temp_update, bmd.updated_at)

    def test_that_save_can_update_two_or_more_times(self):
        """
        Check if save method updates 'updated_at' two times
        """
        bmd = BaseModel()
        sleep(0.05)
        temp_update = bmd.updated_at
        bmd.save()
        sleep(0.05)
        temp1_update = bmd.updated_at
        self.assertLess(temp_update, temp1_update)
        sleep(0.03)
        bmd.save()
        self.assertLess(temp1_update, bmd.updated_at)

    def test_save_update_file(self):
        """
        Check if file is updated when the 'save' method is called
        """
        bmd = BaseModel()
        bmd.save()
        bm_id = "BaseModel.{}".format(bmd.id)
        with open("file.json", encoding="utf-8") as f:
            self.assertIn(bm_id, f.read())

    def test_to_dict_keys(self):
        """
        Checks whether to_dict() returns the expected key
        """
        obj_dict = BaseModel().to_dict()
        attrs = ("id", "created_at", "updated_at", "__class__")
        for attr in attrs:
            self.assertIn(attr, obj_dict)

    def test_to_dict_added_attributes(self):
        """
        Checks if new attributes are returned by to_dict()
        """
        bmd = BaseModel()
        attrs = ["id", "created_at", "updated_at", "__class__"]
        bmd.name = "AirBnB"
        bmd.email = "bnbair@gmail.com"
        attrs.extend(["name", "email"])
        for attr in attrs:
            self.assertIn(attr, bmd.to_dict())

    def test_to_dict_output(self):
        """
        Checks the output returned by to_dict()
        """
        bmd = BaseModel()
        obj_dt = datetime.now()
        bmd.id = "599"
        bmd.created_at = bmd.updated_at = obj_dt
        test_dict = {
            'id': "599",
            'created_at': obj_dt.isoformat(),
            'updated_at': obj_dt.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(test_dict, bmd.to_dict())

    def test_to_dict_with_args(self):
        """
        Checks that TypeError is returned when argument is passed to to_dict()
        """
        bmd = BaseModel()
        with self.assertRaises(TypeError):
            bmd.to_dict(None)

    def test_to_dict_not_dunder_dict(self):
        """Checks that to_dict() is a dict object not equal to __dict__"""
        bmd = BaseModel()
        self.assertNotEqual(bmd.to_dict(), bmd.__dict__)


if __name__ == "__main__":
    unittest.main()
