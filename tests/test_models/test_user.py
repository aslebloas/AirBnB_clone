#!/usr/bin/python3
"""Unitest for User class"""
import json
import os
import unittest

from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class TestUserInit(unittest.TestCase):
    """Test for User Instance Initialization"""
    def setUp(self):
        """setup method for the tests in the class"""
        self.user1 = User()
        self.user1.first_name = "Betty"
        self.user1.last_name = "Holberton"
        self.user1.email = "airbnb@holbertonschool.com"
        self.user1.password = "root"
        self.user1.my_number = 89

        self.user2 = User()

    def test_attr_id(self):
        """test if attribute id are correctly set up"""
        self.assertIs(type(self.user1.id), str)
        self.assertNotEqual(self.user1.id, self.user2.id)

    def test_attr_created_at(self):
        """test if attribute created_at are correctly set up"""
        self.assertIs(type(self.user1.created_at), datetime)
        self.assertIs(type(self.user2.created_at), datetime)

    def test_attr_first_name(self):
        """test if attribute firt_name are correctly set up"""
        self.assertIs(type(self.user1.first_name), str)
        self.assertEqual(self.user1.first_name, "Betty")
        self.assertIs(type(self.user2.first_name), str)
        self.assertEqual(self.user2.first_name, "")

    def test_attr_last_name(self):
        """test if attribute last_name are correctly set up"""
        self.assertIs(type(self.user1.last_name), str)
        self.assertEqual(self.user1.last_name, "Holberton")
        self.assertIs(type(self.user2.last_name), str)
        self.assertEqual(self.user2.last_name, "")

    def test_attr_email(self):
        """test if attribute email are correctly set up"""
        self.assertIs(type(self.user1.email), str)
        self.assertEqual(self.user1.email, "airbnb@holbertonschool.com")
        self.assertIs(type(self.user2.email), str)
        self.assertEqual(self.user2.email, "")

    def test_attr_password(self):
        """test if attribute password are correctly set up"""
        self.assertIs(type(self.user1.password), str)
        self.assertEqual(self.user1.password, "root")
        self.assertIs(type(self.user2.password), str)
        self.assertEqual(self.user2.password, "")

    def test_attr_my_number(self):
        """test if attribute my_number are correctly set up"""
        self.assertIs(type(self.user1.my_number), int)
        self.assertEqual(self.user1.my_number, 89)
        with self.assertRaises(AttributeError):
            self.assertIs(getattr(self.user2, 'my_number'))

    def test_kwargs(self):
        """test create User from dictionary"""
        self.user_dic = self.user2.to_dict()
        self.user3 = User(**self.user_dic)
        self.user4 = User({})
        self.assertIs(type(self.user3.created_at), datetime)
        self.assertIsNot(self.user3, self.user2)
        self.assertEqual(self.user3.id, self.user2.id)
        self.assertEqual(self.user3.created_at, self.user2.created_at)
        self.assertNotIn('updated_at', self.user_dic)
        self.assertIn('id', self.user4.__dict__)
        #TODO: test if dic is not compliant? ie: no id...

    def test_str(self):
        """test str method"""
        self.user_dic = self.user2.to_dict()
        self.user3 = User(**self.user_dic)
        self.assertEqual(str(self.user2), str(self.user3))

    def tearDown(self):
        """teardown objects"""
        pass


class TestUserMethods(unittest.TestCase):
    """Test for User methods"""
    path = os.path.abspath("file.json")
    test_path = os.path.abspath("test_file.json")
    flag = 0

    @classmethod
    def setUpClass(cls):
        """Setup class instances"""
        # if file.json exists
        if os.path.exists(TestUserMethods.path) is True:
            # if copy of file.json exists delete it
            if os.path.exists(TestUserMethods.test_path) is True:
                os.remove(TestUserMethods.test_path)
            # copy content of file.json to test_file.json
            os.rename(TestUserMethods.path,
                      TestUserMethods.test_path)
        else:
            TestUserMethods.flag = 1

    @classmethod
    def tearDownClass(cls):
        """Teardown class instances"""
        # if copy of file.json exists and is not empty
        if (os.path.exists(TestUserMethods.test_path)) is True:
            # remove file.json
            os.remove(TestUserMethods.path)
            # copy content of test_file.json to file.json
            os.rename(TestUserMethods.test_path,
                      TestUserMethods.path)
        if TestUserMethods.flag == 1:
            os.remove(TestUserMethods.path)

    def setUp(self):
        """setup method for the tests in the class"""
        self.user1 = User()
        self.user1.name = "Holberton"
        self.user1.my_number = 89
        self.user2 = User()
        self.user2.name = "Betty"
        self.user2.my_number = 98

    def test_save(self):
        """test save User instance method"""
        self.user2.save()
        self.assertNotIn('updated_at', self.user1.__dict__)
        self.user1.save()
        self.assertIn('updated_at', self.user1.__dict__)
        self.assertIs(type(self.user1.updated_at), datetime)
        self.assertIs(type(self.user1.created_at), datetime)
        self.assertEqual(self.user1.created_at < self.user1.updated_at, True)
        self.assertEqual(self.user1.created_at < self.user2.created_at, True)

    def test_to_dict(self):
        """test to_dict User instance method"""
        self.user1.save()
        self.user1_json = self.user1.to_dict()
        self.assertIs(type(self.user1_json['my_number']), int)
        self.assertEqual(self.user1_json['my_number'], 89)
        self.assertIs(type(self.user1_json['name']), str)
        self.assertEqual(self.user1_json['name'], "Holberton")
        self.assertIs(type(self.user1_json['__class__']), str)
        self.assertEqual(self.user1_json['__class__'], "User")
        self.assertIs(type(self.user1_json['created_at']), str)
        self.assertIs(type(self.user1_json['updated_at']), str)
        self.assertIs(type(self.user1_json['id']), str)

    def test_json(self):
        """test formatting in the json file"""
        self.user1.save()
        with open(TestUserMethods.path) as file:
            self.assertIs(os.path.exists(TestUserMethods.path), True)
            self.json_dict = json.load(file)
            for k, v in self.json_dict.items():
                for key, value in v.items():
                    if key == "created_at":
                        self.assertIs(type(value), str)
                    elif key == "updated_at":
                        self.assertIs(type(value), str)

if __name__ == '__main__':
    unittest.main()
