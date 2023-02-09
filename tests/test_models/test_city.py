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


class TestCityDocs(unittest.TestCase):
    """ check for documentation """
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(City.__doc__) > 0)


class TestCityPep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/city.py'
        file2 = 'tests/test_models/test_city.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestCity(unittest.TestCase):
    """ tests for class City """
    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        cls.city = City()

    def test_subclass(self):
        """ test that city is a subclass of basemodel """
        self.assertIsInstance(self.city, BaseModel)
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_id(self):
        """ test id """
        self.assertEqual(str, type(self.city.id))

    def test_created_at(self):
        """ test created_at """
        self.assertEqual(datetime, type(self.city.created_at))

    def test_updated_at(self):
        """ test updated_at """
        self.assertEqual(datetime, type(self.city.updated_at))

    def test_name(self):
        """ test name """
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.name, "")

    def test_state_id(self):
        """ test state id """
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.state_id, "")

    def test_to_dict(self):
        """ test to_dict method """
        new_dict = self.city.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(self.city))

    def test_str(self):
        """ test ___str___ method """
        correct = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(correct, str(self.city))

    @classmethod
    def tearDownClass(cls):
        """ remove test instances """
        pass
