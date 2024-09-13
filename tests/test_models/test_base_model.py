#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
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
        old_updated_at = self.model.updated_at
        self.model.save()

        # Check that updated_at has been updated to a later time
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertTrue(self.model.updated_at > old_updated_at)

    def test_save_persists_in_storage(self):
        """Test that calling `save` persists the instance in storage."""
        self.model.save()

        key = f"BaseModel.{self.model.id}"
        all_objects = storage.all()

        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key], self.model)

if __name__ == '__main__':
    unittest.main()
