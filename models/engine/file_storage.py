#!/usr/bin/python3
"""
file_storage
=================
serializes instances to a JSON file and deserializes JSON files to instances
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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

        with open(self.__file_path, "w") as f:
            json.dump({k: v.to_dict()\
            for k, v in self.__objects.items()}, f)

    def reload(self):
        """Load and deserialize the JSON file to objects if it exists"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    cls = globals().get(class_name)
                    if cls:
                        self.__objects[key] = cls(**value)
    def classes(self):
        return {
            "State": State,
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "Review": Review,
            "Amenity": Amenity,
            "Place": Place
        }
