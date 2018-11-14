#!/usr/bin/python3
"""Unitest for BaseModel class"""

import unittest
from models.city import City
from datetime import datetime


class TestCityModelInit(unittest.TestCase):
    """Test for City Instance Initialization"""
    def setUp(self):
        """setup method for the tests in the class"""
        self.model1 = City()
        self.model1.name = "Holberton"
        self.model1.my_number = 89
        self.model2 = City()
        self.model2.name = "Betty"
        self.model2.my_number = 98
        self.model2.state_id = "cally"

    def test_attr_state_id(self):
        """Tests attribute state Id"""
        self.assertIs(type(self.model1.state_id), str)
        self.assertEqual(self.model1.state_id, '')
        self.assertEqual(self.model2.state_id, 'cally')

    def test_attr_id(self):
        """test if attribute id are correctly set up"""
        self.assertIs(type(self.model1.id), str)
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_attr_created_at(self):
        """test if attribute created_at are correctly set up"""
        self.assertIs(type(self.model1.created_at), datetime)

    def test_attr_name(self):
        """test if attribute name are correctly set up"""
        self.model5 = City()
        self.assertEqual(self.model5.name, '')
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
        """test create City from dictionary"""
        self.model_dic = self.model2.to_dict()
        self.model3 = City(**self.model_dic)
        self.assertIs(type(self.model3.created_at), datetime)
        self.assertIsNot(self.model3, self.model2)
        self.assertEqual(self.model3.id, self.model2.id)
        self.assertEqual(self.model3.created_at, self.model2.created_at)
        self.assertEqual(self.model3.name, self.model2.name)
        self.assertEqual(self.model3.my_number, self.model2.my_number)
        self.assertNotIn('updated_at', self.model_dic)
        #TODO: test if dic is not compliant? ie: no id...

    def test_str(self):
        """test str method"""
        self.model_dic = self.model2.to_dict()
        self.model3 = City(**self.model_dic)
        self.assertEqual(str(self.model2), str(self.model3))

    def tearDown(self):
        """teardown objects"""
        pass


class TestCityModelMethods(unittest.TestCase):
    """Test for City methods"""
    path = os.path.abspath("file.json")
    test_path = os.path.abspath("test_file.json")
    flag = 0

    @classmethod
    def setUpClass(cls):
        """Setup class instances"""
        # if file.json exists
        if os.path.exists(TestCityModelMethods.path) is True:
            # if copy of file.json exists delete it
            if os.path.exists(TestCityModelMethods.test_path) is True:
                os.remove(TestCityModelMethods.test_path)
            # copy content of file.json to test_file.json
            os.rename(TestCityModelMethods.path,
                      TestCityModelMethods.test_path)
        else:
            TestCityModelMethods.flag = 1

    @classmethod
    def tearDownClass(cls):
        """Teardown class instances"""
        # if copy of file.json exists and is not empty
        if (os.path.exists(TestCityModelMethods.test_path)) is True:
            # remove file.json
            os.remove(TestCityModelMethods.path)
            # copy content of test_file.json to file.json
            os.rename(TestCityModelMethods.test_path,
                      TestCityModelMethods.path)
        if TestCityModelMethods.flag == 1:
            os.remove(TestCityModelMethods.path)

    def setUp(self):
        """setup method for the tests in the class"""
        self.model1 = City()
        self.model1.name = "Holberton"
        self.model1.my_number = 89
        self.model2 = City()
        self.model2.name = "Betty"
        self.model2.my_number = 98

    def test_save(self):
        """test save City instance method"""
        self.model2.save()
        self.assertNotIn('updated_at', self.model1.__dict__)
        self.model1.save()
        self.assertIn('updated_at', self.model1.__dict__)
        self.assertIs(type(self.model1.updated_at), datetime)
        self.assertIs(type(self.model1.created_at), datetime)

    def test_to_dict(self):
        """test to_dict City instance method"""
        self.model1.save()
        self.model1_json = self.model1.to_dict()
        self.assertIs(type(self.model1_json['my_number']), int)
        self.assertEqual(self.model1_json['my_number'], 89)
        self.assertIs(type(self.model1_json['name']), str)
        self.assertEqual(self.model1_json['name'], "Holberton")
        self.assertIs(type(self.model1_json['__class__']), str)
        self.assertEqual(self.model1_json['__class__'], "City")
        self.assertIs(type(self.model1_json['created_at']), str)
        self.assertIs(type(self.model1_json['updated_at']), str)
        self.assertIs(type(self.model1_json['id']), str)

if __name__ == '__main__':
    unittest.main()
