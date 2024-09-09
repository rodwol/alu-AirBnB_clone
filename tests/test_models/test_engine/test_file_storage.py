#!/usr/bin/python3
"""

"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Unit tests for the FileStorage class"""

    def setUp(self):
        # set up resources before each test
        self.file_path = "file.json"
        self.storage = FileStorage()
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        # clean up resources after each test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_dict(self):
        """
        Test that all() returns the __objects dictionary.
        """
        self.assertEqual(type(self.storage.all()), dict)

    def test_new_adds_object(self):
        """
        Test that new() correctly adds a BaseModel object to __objects.
        """
        model = BaseModel()
        self.storage.new(model)
        key = f"BaseModel.{model.id}"
        self.assertIn(key, self.storage.all())

    def test_save_serializes_objects(self):
        # save() correctly serializes __objects to a file.
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        
        # Check that the file is created
        self.assertTrue(os.path.exists(self.file_path))

        # Check the contents of the file
        with open(self.file_path, "r") as f:
            data = json.load(f)
            key = f"BaseModel.{model.id}"
            self.assertIn(key, data)

    def test_reload_deserializes_objects(self):
       
        # reload() correctly deserializes objects from a JSON file
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        
        # Ensure that objects are reloaded into __objects
        key = f"BaseModel.{model.id}"
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)

if __name__ == '__main__':
    unittest.main()
