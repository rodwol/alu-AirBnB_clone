#!/usr/bin/python3
"""
base_model
=================

defines the BaseModel class which serves as the base for all other classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    a base class that defines all common attributes for other classes
    in the project
    """

    def __init__(self,  *_args, **kwargs):
        """Initialize a new BaseModel."""

        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid.uuid4())

        if kwargs:
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], time_format)
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], time_format)
            self.__dict__.update(kwargs)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,\
        self.id, self.__dict__)

    def save(self):
        """Set updated_at to current datetime."""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary of BaseModel class"""

        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
