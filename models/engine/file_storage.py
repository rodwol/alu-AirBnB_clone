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

        f = open(self.__file_path, "w")
        text = json.dumps(self.__objects)
        f.write(text)

    def reload(self):
        """Load and deserialize the JSON file to objects if it exists"""

        if isfile(self.__file_path):
            f = open(self.__file_path, "r")
            text = f.read()
            obj_dict = json.loads(text)

        class_map = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "City": City,
            "State": State,
            "Amenity": Amenity,
            "Review": Review
        }
       
        for key, value in obj_dict.items():
            class_name = key.split(".")[0]
            self.__objects[key] = globals()[class_name](**value)
