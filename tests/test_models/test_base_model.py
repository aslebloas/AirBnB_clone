#!/usr/bin/python3
"""Unitest for BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test for BaseModel setup"""
    def setUp(self):
        """setup method for the tests in the class"""
        self.model1 = BaseModel()
        self.model1.name = "Holberton"
        self.model1.my_number = 89
        self.model2 = BaseModel()
        self.model2.name = "Holberton"
        self.model2.my_number = 89

    def test_attributes(self):
        """test if attributest are correctly set up"""
        self.assertIs(type(self.model1.id), str)
        self.assertNotEqual(self.model1.id, self.model2.id)
        self.assertIs(type(self.model1.created_at), datetime)
        self.assertIs(type(self.model1.name), str)
        self.assertEqual(self.model1.name, "Holberton")
        self.assertIs(type(self.model1.my_number), int)
        self.assertEqual(self.model1.my_number, 89)

    def test_save(self):
        """test save BaseModel instance method"""
        self.model2.save()
        self.assertNotIn('updated_at', self.model1.__dict__)
        self.model1.save()
        self.assertIn('updated_at', self.model1.__dict__)
        self.assertIs(type(self.model1.updated_at), datetime)
        self.assertIs(type(self.model1.created_at), datetime)

    def test_to_dict(self):
        """test to_dict BaseModel instance method"""
        self.model1.save()
        self.model1_json = self.model1.to_dict()
        self.assertIs(type(self.model1_json['my_number']), int)
        self.assertEqual(self.model1_json['my_number'], 89)
        self.assertIs(type(self.model1_json['name']), str)
        self.assertEqual(self.model1_json['name'], "Holberton")
        self.assertIs(type(self.model1_json['__class__']), str)
        self.assertEqual(self.model1_json['__class__'], "BaseModel")
        self.assertIs(type(self.model1_json['created_at']), str)
        self.assertIs(type(self.model1_json['updated_at']), str)
        self.assertIs(type(self.model1_json['id']), str)

    def test_kwargs(self):
        """test create BaseModel from dictionary"""
        self.model_json = self.model2.to_dict()
        self.model3 = BaseModel(**self.model_json)
        self.assertIs(type(self.model3.created_at), datetime)
        self.assertIsNot(self.model3, self.model2)

if __name__ == '__main__':
    unittest.main()
