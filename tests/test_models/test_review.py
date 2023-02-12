#!/usr/bin/python3
import unittest
import pep8
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestReviewDocs(unittest.TestCase):
    """ check for documentation """
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(Review.__doc__) > 0)


class TestReviewPep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/review.py'
        file2 = 'tests/test_models/test_review.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestReview(unittest.TestCase):
    """ tests for class Review """
    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        cls.review = Review()

    def test_subclass(self):
        """ test that review is a subclass of basemodel """
        self.assertIsInstance(self.review, BaseModel)
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_id(self):
        """ test id """
        self.assertEqual(str, type(self.review.id))

    def test_created_at(self):
        """ test created_at """
        self.assertEqual(datetime, type(self.review.created_at))

    def test_updated_at(self):
        """ test updated_at """
        self.assertEqual(datetime, type(self.review.updated_at))

    def test_place_id(self):
        """ test place_id """
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(self.review.place_id, "")

    def test_user_id(self):
        """ test user_id """
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(self.review.user_id, "")

    def test_text(self):
        """ test text """
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.text, "")

    def test_to_dict(self):
        """ test to_dict method """
        new_dict = self.review.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(self.review))

    @classmethod
    def tearDownClass(cls):
        """ remove test instances """
        pass
