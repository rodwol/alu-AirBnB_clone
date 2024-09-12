#!/usr/bin/python3
"""
file_storage
=================
serializes instances to a JSON file and deserializes JSON files to instances
"""

import json
from os.path import isfile
from models.base_model import BaseModel


class FileStorage:
    """
    a class that serializes/deserializes instances to/from JSON
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initialize a new FileStorage."""

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Return all objects."""

        return self.__objects

    def new(self, obj):
        """Add/Save a new object."""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """Save the objects to the JSON file."""

        with open(self.__file_path, "w", encoding='UTF-8') as f:
            json.dump({k: v.to_dict() if hasattr(v, "to_dict") else v\
            for k, v in self.__objects.items()}, f)

    def reload(self):
        """Load and deserialize the JSON file to objects if it exists"""

        if isfile(self.__file_path):
            with open(self.__file_path, "r", encoding='UTF-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    cls = globals().get(class_name)
                    if cls:
                        self.__objects[key] = cls(**value)
