#!/usr/bin/python3
"""
file_storage
=================
serializes instances to a JSON file and deserializes JSON files to instances
"""

import json
from os.path import isfile


class FileStorage:
    """
    a class that serializes/deserializes instances to/from JSON
    """

    def __init__(self):
        """Initialize a new FileStorage."""

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Return all objects."""

        return self.__objects

    def new(self, obj):
        """Add/Save a new object."""

        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """Save the objects to the JSON file."""

        f = open(self.__file_path, "w")
        text = json.dumps(self.__objects)
        f.write(text)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value['__class__']
                    if cls_name == "BaseModel":
                        # Recreate the object using BaseModel
                        FileStorage.__objects[key] = BaseModel(**value)
