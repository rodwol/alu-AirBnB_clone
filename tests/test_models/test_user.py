#!/usr/bin/python3
""" Module Documentation """
import unittest
from models.user import User


class testuser(unittest.TestCase):
    """ class docmentation """
    def test_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
