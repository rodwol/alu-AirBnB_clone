#!/usr/bin/python3
"""
Module document
"""
import unittest
from models.state import State


class teststate(unittest.TestCase):
    """ class document """
    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")
