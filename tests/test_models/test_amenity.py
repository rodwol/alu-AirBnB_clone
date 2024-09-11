#!/usr/bin/python3
""" Module documentation """
import unittest
from models.amenity import Amenity


class testamenity(unittest.TestCase):
    """ class documentation """
    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
