#!/usr/bin/python3
import unittest
import pep8
import json
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelDocs(unittest.TestCase):
    """ check for documentation """
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)


class TestBaseModelPep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base_model.py'
        file2 = 'tests/test_models/test_base_model.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestBaseModel(unittest.TestCase):
    """ tests for class BaseModel """
    @classmethod
    def setUpClass(cls):
        """ set up instances for all tests """
        cls.basemodel = BaseModel()

    def test_id(self):
        """ test id """
        self.assertEqual(str, type(self.basemodel.id))

    def test_created_at(self):
        """ test created_at """
        self.assertEqual(datetime, type(self.basemodel.created_at))

    def test_updated_at(self):
        """ test updated_at """
        self.assertEqual(datetime, type(self.basemodel.updated_at))

    def test_to_dict(self):
        """ test to_dict method """
        new_dict = self.basemodel.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(self.basemodel))

    @classmethod
    def tearDownClass(cls):
        """ remove test instances """
        pass
