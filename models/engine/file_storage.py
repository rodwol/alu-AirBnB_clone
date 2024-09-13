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
        self.__objects[key] = obj

    def save(self):
        """Save the objects to the JSON file."""

        odict = self.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Load and deserialize the JSON file to objects if it exists"""

        try:
            with open(self.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

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
