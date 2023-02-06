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


class TestPlaceDocs(unittest.TestCase):
    """ check for documentation """
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(Place.__doc__) > 0)


class TestPlacePep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/place.py'
        file2 = 'tests/test_models/test_place.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestPlace(unittest.TestCase):
    """ tests for class Place """
    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        cls.place = Place()

    def test_subclass(self):
        """ test that place is a subclass of basemodel """
        self.assertIsInstance(self.place, BaseModel)
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))

    def test_id(self):
        """ test id """
        self.assertEqual(str, type(self.place.id))

    def test_created_at(self):
        """ test created_at """
        self.assertEqual(datetime, type(self.place.created_at))

    def test_updated_at(self):
        """ test updated_at """
        self.assertEqual(datetime, type(self.place.updated_at))

    def test_city_id(self):
        """ test city_id """
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(self.place.city_id, "")

    def test_user_id(self):
        """ test user_id """
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(self.place.user_id, "")

    def test_name(self):
        """ test name """
        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(self.place.name, "")

    def test_description(self):
        """ test description """
        self.assertTrue(hasattr(self.place, "description"))
        self.assertEqual(self.place.description, "")

    def test_number_rooms(self):
        """ test number_rooms """
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms(self):
        """ test number_bathrooms """
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest(self):
        """ test max_guest """
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        """ test price_by_night """
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude(self):
        """ test latitude """
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude(self):
        """ test longitude """
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids(self):
        """ test amenity_ids """
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.amenity_ids, [])

    def test_to_dict(self):
        """ test to_dict method """
        new_dict = self.place.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(self.place))

    def test_str(self):
        """ test ___str___ method """
        correct = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(correct, str(self.place))

    @classmethod
    def tearDownClass(cls):
        """ remove test instances """
        pass
