#!/usr/bin/python3
"""Unitest for BaseModel class"""

import unittest
from models.review import Review
from datetime import datetime


class TestReviewModelInit(unittest.TestCase):
    """Test for Review Instance Initialization"""
    def setUp(self):
        """setup method for the tests in the class"""
        self.model1 = Review()
        self.model1.name = "Holberton"
        self.model1.my_number = 89
        self.model1.place_id = "traphouse"
        self.model1.user_id = "killer mike"
        self.model1.text = "great place to trap"
        self.model2 = Review()
        self.model2.name = "Betty"
        self.model2.my_number = 98
        self.model2.place_id = "mantion"
        self.model2.user_id = "Bill Gates"
        self.model2.text = "luxury"
        self.model5 = Review()

    def test_att_place_id(self):
        """tests attribuet place_id"""
        self.assertIs(type(self.model1.text), str)
        self.assertIs(type(self.model2.text), str)
        self.assertIs(type(self.model5.text), str)
        self.assertEqual(self.model1.text, "great place to trap")
        self.assertEqual(self.model2.text, "luxury")
        self.assertEqual(self.model5.text, '')

    def test_att_user_id(self):
        """tests attribuet user_id"""
        self.assertIs(type(self.model1.user_id), str)
        self.assertIs(type(self.model2.user_id), str)
        self.assertIs(type(self.model5.user_id), str)
        self.assertEqual(self.model1.user_id, "killer mike")
        self.assertEqual(self.model2.user_id, "Bill Gates")
        self.assertEqual(self.model5.user_id, '')

    def test_att_place_id(self):
        """tests attribuet place_id"""
        self.assertIs(type(self.model1.place_id), str)
        self.assertIs(type(self.model2.place_id), str)
        self.assertIs(type(self.model5.place_id), str)
        self.assertEqual(self.model1.place_id, "traphouse")
        self.assertEqual(self.model2.place_id, "mantion")
        self.assertEqual(self.model5.place_id, '')

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
        """test create Review from dictionary"""
        self.model_dic = self.model2.to_dict()
        self.model3 = Review(**self.model_dic)
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
        self.model3 = Review(**self.model_dic)
        self.assertEqual(str(self.model2), str(self.model3))

    def tearDown(self):
        """teardown objects"""
        pass


class TestReviewModelMethods(unittest.TestCase):
    """Test for review methods"""
    def setUp(self):
        """setup method for the tests in the class"""
        self.model1 = Review()
        self.model1.name = "Holberton"
        self.model1.my_number = 89
        self.model2 = Review()
        self.model2.name = "Betty"
        self.model2.my_number = 98

    def test_save(self):
        """test save Review instance method"""
        self.model2.save()
        self.assertNotIn('updated_at', self.model1.__dict__)
        self.model1.save()
        self.assertIn('updated_at', self.model1.__dict__)
        self.assertIs(type(self.model1.updated_at), datetime)
        self.assertIs(type(self.model1.created_at), datetime)

    def test_to_dict(self):
        """test to_dict REveiw instance method"""
        self.model1.save()
        self.model1_json = self.model1.to_dict()
        self.assertIs(type(self.model1_json['my_number']), int)
        self.assertEqual(self.model1_json['my_number'], 89)
        self.assertIs(type(self.model1_json['name']), str)
        self.assertEqual(self.model1_json['name'], "Holberton")
        self.assertIs(type(self.model1_json['__class__']), str)
        self.assertEqual(self.model1_json['__class__'], "Review")
        self.assertIs(type(self.model1_json['created_at']), str)
        self.assertIs(type(self.model1_json['updated_at']), str)
        self.assertIs(type(self.model1_json['id']), str)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
