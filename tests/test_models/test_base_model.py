#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import models
from time import sleep
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up method to initialize objects before each test"""
        self.my_model = BaseModel()

    def test_unique_id(self):
        """Test if the id is a unique string"""
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(uuid.UUID(self.my_model.id), uuid.UUID)

    def test_created_at(self):
        """Test that created_at is a datetime object"""
        self.assertIsInstance(self.my_model.created_at, datetime)

    def test_updated_at(self):
        """Test that updated_at is a datetime object"""
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_save_method(self):
        """Test the save method to update 'updated_at' attribute"""
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method to ensure proper dictionary conversion"""
        my_model_json = self.my_model.to_dict()

        self.assertIsInstance(my_model_json, dict)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)

        # Check date format (ISO format)
        self.assertEqual(self.my_model.created_at.isoformat(), my_model_json['created_at'])
        self.assertEqual(self.my_model.updated_at.isoformat(), my_model_json['updated_at'])

    def test_str_method(self):
        """Test the __str__ method for proper output"""
        str_output = str(self.my_model)
        expected_output = "[BaseModel] ({}) {}".format(self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str_output, expected_output)

    def test_kwargs_initialization(self):
        """Test that the class can be initialized with kwargs"""
        my_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_dict)
        self.assertEqual(new_model.id, self.my_model.id)
        self.assertEqual(new_model.created_at, self.my_model.created_at)
        self.assertEqual(new_model.updated_at, self.my_model.updated_at)
        self.assertEqual(new_model.to_dict(), self.my_model.to_dict())
    def test_save_updates_updated_at(self):
        """Test that calling `save` updates the `updated_at` attribute."""
        old_updated_at = self.my_model.updated_at
        self.my_model.save()

        # Check that updated_at has been updated to a later time
        self.assertNotEqual(self.my_model.updated_at, old_updated_at)
        self.assertTrue(self.my_model.updated_at > old_updated_at)

    def test_save_persists_in_storage(self):
        """Test that calling `save` persists the instance in storage."""
        self.my_model.save()

        key = f"BaseModel.{self.my_model.id}"
        all_objects = models.storage.all()

        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key], self.my_model)

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

if __name__ == '__main__':
    unittest.main()
