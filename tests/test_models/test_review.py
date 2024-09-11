#!/usr/bin/python3
""" Module Documentation """
import unittest
from models.review import Review


class testreview(unittest.TestCase):
    """ Class Documentation """
    def test_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

