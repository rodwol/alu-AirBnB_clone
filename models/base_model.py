#!/usr/bin/python3
"""
base_model
=================

defines the BaseModel class which serves as the base for all other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    a base class that defines all common attributes for other classes
    in the project
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
        self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
