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

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self)
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        """Test that __file_path is a private string attribute."""
        fs = FileStorage()  # Create an instance of FileStorage
        self.assertEqual(str, type(fs._FileStorage__file_path))

    def test_FileStorage_objects_is_private_dict(self):
        """Test that __objects is a private dictionary attribute."""
        fs = FileStorage()
        self.assertEqual(dict, type(fs._FileStorage__objects))

    def test_storage_initializes(self):
        """Test that the storage object is an instance of FileStorage."""
        self.assertEqual(type(models.storage), FileStorage)
    def test_reload_no_file(self):
        """Test reload when the JSON file doesn't exist."""
        # Ensure no file exists
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

        # Call reload (should do nothing)
        self.file_storage.reload()

        # __objects should remain empty
        self.assertEqual(self.file_storage._FileStorage__objects, {})

    def test_reload_with_file(self):
        """Test reload when the JSON file exists and contains valid data."""
        # Create a BaseModel object and save it to a dict
        base_model = BaseModel()
        obj_dict = {f"BaseModel.{base_model.id}": base_model.to_dict()}

        # Write the dict to the temp file in JSON format
        with open(self.temp_file, "w") as f:
            json.dump(obj_dict, f)

        # Call reload (should populate __objects with deserialized data)
        self.file_storage.reload()

        # __objects should contain the BaseModel object we serialized
        objects = self.file_storage._FileStorage__objects
        self.assertIn(f"BaseModel.{base_model.id}", objects)

        # Ensure the object deserialized correctly
        self.assertEqual(objects[f"BaseModel.{base_model.id}"].id, base_model.id)


if __name__ == '__main__':
    unittest.main()
