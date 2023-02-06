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


class TestUserDocs(unittest.TestCase):
    """ check for documentation """
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(User.__doc__) > 0)


class TestUserPep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/user.py'
        file2 = 'tests/test_models/test_user.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestUser(unittest.TestCase):
    """ tests for class User """
    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        cls.user = User()

    def test_subclass(self):
        """ test that user is a subclass of basemodel """
        self.assertIsInstance(self.user, BaseModel)
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_id(self):
        """ test id """
        self.assertEqual(str, type(self.user.id))

    def test_created_at(self):
        """ test created_at """
        self.assertEqual(datetime, type(self.user.created_at))

    def test_updated_at(self):
        """ test updated_at """
        self.assertEqual(datetime, type(self.user.updated_at))

    def test_email(self):
        """ test email """
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(self.user.email, "")

    def test_password(self):
        """ test password """
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(self.user.password, "")

    def test_first_name(self):
        """ test first_name """
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(self.user.first_name, "")

    def test_last_name(self):
        """ test last_name """
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.last_name, "")

    def test_to_dict(self):
        """ test to_dict method """
        new_dict = self.user.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(self.user))

    def test_str(self):
        """ test ___str___ method """
        correct = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(correct, str(self.user))

    @classmethod
    def tearDownClass(cls):
        """ remove test instances """
        pass
