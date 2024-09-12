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
        self.model = BaseModel()

        FileStorage._FileStorage__objects = {}

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
        key = "BaseModel.{}".format(model.id)
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
            key = "BaseModel.{}".format(model.id)
            self.assertIn(key, data)

    def test_reload_deserializes_objects(self):
       
        # reload() correctly deserializes objects from a JSON file
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        
        # Ensure that objects are reloaded into __objects
        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)

    def test_save_c(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.storage.new(model1)
        self.storage.new(model2)
        self.storage.save()

        # Check that the file is created
        self.assertTrue(os.path.exists(self.file_path))

        # Check the contents of the file
        with open(self.file_path, "r") as f:
            data = json.load(f)
            key1 = "BaseModel.{}".format(model1.id)
            key2 = "BaseModel.{}".format(model2.id)
            self.assertIn(key1, data)
            self.assertIn(key2, data)
            self.assertEqual(data[key1]['id'], model1.id)
            self.assertEqual(data[key2]['id'], model2.id)

    def test_file_path(self):
        """Test if the __file_path attribute is correctly set"""
        expected_file_path = "file.json"
        self.assertEqual(getattr(self.storage,\
        "_FileStorage__file_path"), expected_file_path)

    def test_objects_initialization(self):
        self.assertEqual(getattr(self.storage,\
        "_FileStorage__objects"), {})

if __name__ == '__main__':
    unittest.main()
