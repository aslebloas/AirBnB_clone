#!/usr/bin/python3
"""Unitest for BaseModel class"""
import json
import os
import unittest

from models.base_model import BaseModel
from datetime import datetime


class TestBaseModelInit(unittest.TestCase):
    """Test for BaseModel Instance Initialization"""
    def setUp(self):
        """setup method for the tests in the class"""
        self.model1 = BaseModel()
        self.model1.name = "Holberton"
        self.model1.my_number = 89
        self.model2 = BaseModel()
        self.model2.name = "Betty"
        self.model2.my_number = 98
        self.dic25 = {'name': 'Erwin', 'my_number': 42,
                                 'state_id': 'CA', 'test': 'test'}
        self.model3 = BaseModel(**self.dic25)

    def test_dict_init(self):
        """testing the dictionary initilization of this model"""
        self.assertIs(type(self.model3.name), str)
        self.assertEqual(self.model3.name, "Erwin")
        self.assertIs(type(self.model3.my_number), int)
        self.assertEqual(self.model3.my_number, 42)
        self.assertIs(type(self.model3.test), str)
        self.assertEqual(self.model3.test, "test")

    def test_attr_id(self):
        """test if attribute id are correctly set up"""
        self.assertIs(type(self.model1.id), str)
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_attr_created_at(self):
        """test if attribute created_at are correctly set up"""
        self.assertIs(type(self.model1.created_at), datetime)

    def test_attr_name(self):
        """test if attribute name are correctly set up"""
        self.assertIs(type(self.model1.name), str)
        self.assertEqual(self.model1.name, "Holberton")
        self.assertIs(type(self.model2.name), str)
        self.assertEqual(self.model2.name, "Betty")

    def test_attr_my_number(self):
        """test if attribute my_number are correctly set up"""
        self.assertIs(type(self.model1.my_number), int)
        self.assertEqual(self.model1.my_number, 89)
        self.assertIs(type(self.model2.my_number), int)
        self.assertEqual(self.model2.my_number, 98)

    def test_kwargs(self):
        """test create BaseModel from dictionary"""
        self.model_dic = self.model2.to_dict()
        self.model3 = BaseModel(**self.model_dic)
        self.model4 = BaseModel({})
        self.assertIs(type(self.model3.created_at), datetime)
        self.assertIsNot(self.model3, self.model2)
        self.assertEqual(self.model3.id, self.model2.id)
        self.assertEqual(self.model3.created_at, self.model2.created_at)
        self.assertEqual(self.model3.name, self.model2.name)
        self.assertEqual(self.model3.my_number, self.model2.my_number)
        self.assertNotIn('updated_at', self.model_dic)
        self.assertIn('id', self.model4.__dict__)
        #TODO: test if dic is not compliant? ie: no id...

    def test_str(self):
        """test str method"""
        self.model_dic = self.model2.to_dict()
        self.model3 = BaseModel(**self.model_dic)
        self.assertEqual(str(self.model2), str(self.model3))

    def tearDown(self):
        """teardown objects"""
        pass


class TestBaseModelMethods(unittest.TestCase):
    """Test for BaseModel methods"""
    path = os.path.abspath("file.json")
    test_path = os.path.abspath("test_file.json")
    flag = 0

    @classmethod
    def setUpClass(cls):
        """Setup class instances"""
        # if file.json exists
        if os.path.exists(TestBaseModelMethods.path) is True:
            # if copy of file.json exists delete it
            if os.path.exists(TestBaseModelMethods.test_path) is True:
                os.remove(TestBaseModelMethods.test_path)
            # copy content of file.json to test_file.json
            os.rename(TestBaseModelMethods.path,
                      TestBaseModelMethods.test_path)
        else:
            TestBaseModelMethods.flag = 1

    @classmethod
    def tearDownClass(cls):
        """Teardown class instances"""
        # if copy of file.json exists and is not empty
        if (os.path.exists(TestBaseModelMethods.test_path)) is True:
            # remove file.json
            os.remove(TestBaseModelMethods.path)
            # copy content of test_file.json to file.json
            os.rename(TestBaseModelMethods.test_path,
                      TestBaseModelMethods.path)
        if TestBaseModelMethods.flag == 1:
            os.remove(TestBaseModelMethods.path)

    def setUp(self):
        """setup method for the tests in the class"""
        self.model1 = BaseModel()
        self.model1.name = "Holberton"
        self.model1.my_number = 89
        self.model2 = BaseModel()
        self.model2.name = "Betty"
        self.model2.my_number = 98

    def test_save(self):
        """test save BaseModel instance method"""
        self.model2.save()
        self.assertNotIn('updated_at', self.model1.__dict__)
        self.model1.save()
        self.assertIn('updated_at', self.model1.__dict__)
        self.assertIs(type(self.model1.updated_at), datetime)
        self.assertIs(type(self.model1.created_at), datetime)
        self.assertEqual(self.model1.created_at < self.model1.updated_at, True)
        self.assertEqual(self.model1.created_at < self.model2.created_at, True)

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

    def test_json(self):
        """test formatting in the json file"""
        self.model1.save()
        with open(TestBaseModelMethods.path) as file:
            self.assertIs(os.path.exists(TestBaseModelMethods.path), True)
            self.json_dict = json.load(file)
            for k, v in self.json_dict.items():
                for key, value in v.items():
                    if key == "created_at":
                        self.assertIs(type(value), str)
                    elif key == "updated_at":
                        self.assertIs(type(value), str)

if __name__ == '__main__':
    unittest.main()
