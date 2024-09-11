#!/usr/bin/python3
"""
module representing review in the project
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ class representing review """
    place_id = ""
    user_id = ""
    test = ""
