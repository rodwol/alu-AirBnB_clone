#!/usr/bin/python3
"""
Module Document
"""
import unittest
from models.city import City


class testcity(unittest.TestCase):
    """ class documentation """
    def test_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
