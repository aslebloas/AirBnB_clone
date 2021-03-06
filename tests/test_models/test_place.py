#!/usr/bin/python3
"""Unitest for BaseModel class"""


from shutil import copyfile
import os
import json
import unittest
from models.place import Place
from datetime import datetime


class TestPlaceModelInit(unittest.TestCase):
    """Test for Place Instance Initialization"""
    def setUp(self):
        """setup method for the tests in the class"""
        self.model1 = Place()
        self.model1.name = "Holberton"
        self.model1.my_number = 89
        self.model1.city_id = "SanFran"
        self.model1.user_id = "Bob"
        self.model1.description = "shit hole"
        self.model1.number_rooms = 1
        self.model1.number_bathrooms = 1
        self.model1.max_guest = 5
        self.model1.price_by_night = 32
        self.model1.latitude = 55.55
        self.model1.longitude = 55.55
        self.model1.amenity_ids = ["bed", 'tv']
        self.model2 = Place()
        self.model2.name = "Betty"
        self.model2.my_number = 98
        self.model2.city_id = "Eurika"
        self.model2.user_id = "Fred"
        self.model2.description = "mantion"
        self.model2.number_rooms = 32
        self.model2.number_bathrooms = 40
        self.model2.max_guest = 64
        self.model2.price_by_night = 1000
        self.model2.latitude = 88.88
        self.model2.longitude = 88.88
        self.model2.amenity_ids = ['everything']
        self.dic25 = {'city_id': 'SanFran', 'user_id': 'Gove',
                      'description': 'nice', 'number_rooms': 7,
                      'number_bathrooms': 7, 'max_guest': 7,
                      'price_by_night': 7, 'longitude': 7.7,
                      'latitude': 7.7, 'amenity_ids': ['bla', 'bla'],
                      'name': 'Erwin', 'my_number': 42, 'state_id': 'CA',
                      'test': 'test'}
        self.model3 = Place(**self.dic25)

    def test_dict_init(self):
        """testing the dictionary initilization of this model"""
        self.assertIs(type(self.model3.name), str)
        self.assertEqual(self.model3.name, "Erwin")
        self.assertIs(type(self.model3.my_number), int)
        self.assertEqual(self.model3.my_number, 42)
        self.assertIs(type(self.model3.test), str)
        self.assertEqual(self.model3.test, "test")
        self.assertIs(type(self.model3.city_id), str)
        self.assertEqual(self.model3.city_id, 'SanFran')
        self.assertIs(type(self.model3.user_id), str)
        self.assertEqual(self.model3.user_id, 'Gove')
        self.assertIs(type(self.model3.description), str)
        self.assertEqual(self.model3.description, 'nice')
        self.assertIs(type(self.model3.number_rooms), int)
        self.assertEqual(self.model3.number_rooms, 7)
        self.assertIs(type(self.model3.number_bathrooms), int)
        self.assertEqual(self.model3.number_bathrooms, 7)
        self.assertIs(type(self.model3.max_guest), int)
        self.assertEqual(self.model3.max_guest, 7)
        self.assertIs(type(self.model3.price_by_night), int)
        self.assertEqual(self.model3.price_by_night, 7)
        self.assertIs(type(self.model3.latitude), float)
        self.assertEqual(self.model3.latitude, 7.7)
        self.assertIs(type(self.model3.longitude), float)
        self.assertEqual(self.model3.longitude, 7.7)
        self.assertIs(type(self.model3.amenity_ids), list)
        self.assertEqual(self.model3.amenity_ids, ['bla', 'bla'])

    def test_attr_amenity_ids(self):
        """tests attribute amenity_ids"""
        self.assertIs(type(self.model1.amenity_ids), list)
        self.assertIs(type(self.model2.amenity_ids), list)
        self.assertEqual(self.model1.amenity_ids, ["bed", 'tv'])
        self.assertEqual(self.model2.amenity_ids, ["everything"])

    def test_attr_longitude(self):
        """tests attribute longitude"""
        self.assertIs(type(self.model1.longitude), float)
        self.assertIs(type(self.model2.longitude), float)
        self.assertEqual(self.model1.longitude, 55.55)
        self.assertEqual(self.model2.longitude, 88.88)

    def test_attr_latitude(self):
        """tests attribute latitude"""
        self.assertIs(type(self.model1.latitude), float)
        self.assertIs(type(self.model2.latitude), float)
        self.assertEqual(self.model1.latitude, 55.55)
        self.assertEqual(self.model2.latitude, 88.88)

    def test_attr_price_by_night(self):
        """tests attribute price_by_night"""
        self.assertIs(type(self.model1.price_by_night), int)
        self.assertIs(type(self.model2.price_by_night), int)
        self.assertEqual(self.model1.price_by_night, 32)
        self.assertEqual(self.model2.price_by_night, 1000)

    def test_attr_max_guest(self):
        """tests attribute max_guests"""
        self.assertIs(type(self.model1.max_guest), int)
        self.assertIs(type(self.model2.max_guest), int)
        self.assertEqual(self.model1.max_guest, 5)
        self.assertEqual(self.model2.max_guest, 64)

    def test_attr_number_bathrooms(self):
        """tests attribute number_bathrooms"""
        self.assertIs(type(self.model1.number_bathrooms), int)
        self.assertIs(type(self.model2.number_bathrooms), int)
        self.assertEqual(self.model1.number_bathrooms, 1)
        self.assertEqual(self.model2.number_bathrooms, 40)

    def test_attr_number_rooms(self):
        """tests attribute number_rooms"""
        self.assertIs(type(self.model1.number_rooms), int)
        self.assertIs(type(self.model2.number_rooms), int)
        self.assertEqual(self.model1.number_rooms, 1)
        self.assertEqual(self.model2.number_rooms, 32)

    def test_attr_description(self):
        """tests attribute description"""
        self.assertIs(type(self.model1.description), str)
        self.assertIs(type(self.model2.description), str)
        self.assertEqual(self.model1.description, 'shit hole')
        self.assertEqual(self.model2.description, 'mantion')

    def test_attr_user_id(self):
        """ tests attribute user_id"""
        self.assertIs(type(self.model1.user_id), str)
        self.assertIs(type(self.model2.user_id), str)
        self.assertEqual(self.model1.user_id, 'Bob')
        self.assertEqual(self.model2.user_id, 'Fred')

    def test_attr_city_id(self):
        """tests attribute city_id"""
        self.assertIs(type(self.model1.city_id), str)
        self.assertIs(type(self.model2.city_id), str)
        self.assertEqual(self.model1.city_id, "SanFran")
        self.assertEqual(self.model2.city_id, "Eurika")

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
        self.model3 = Place(**self.model_dic)
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
        self.model3 = Place(**self.model_dic)
        self.assertEqual(str(self.model2), str(self.model3))

    def tearDown(self):
        """teardown objects"""
        pass


class TestPlaceModelMethods(unittest.TestCase):
    """Test for Place methods"""
    path = os.path.abspath("file.json")
    test_path = os.path.abspath("test_file.json")
    flag = 0

    @classmethod
    def setUpClass(cls):
        """Setup class instances"""
        # if file.json exists
        if os.path.exists(TestPlaceModelMethods.path) is True:
            # if copy of file.json exists delete it
            if os.path.exists(TestPlaceModelMethods.test_path) is True:
                os.remove(TestPlaceModelMethods.test_path)
            # copy content of file.json to test_file.json
            os.rename(TestPlaceModelMethods.path,
                      TestPlaceModelMethods.test_path)
        else:
            TestPlaceModelMethods.flag = 1

    @classmethod
    def tearDownClass(cls):
        """Teardown class instances"""
        # if copy of file.json exists and is not empty
        if (os.path.exists(TestPlaceModelMethods.test_path)) is True:
            # remove file.json
            os.remove(TestPlaceModelMethods.path)
            # copy content of test_file.json to file.json
            os.rename(TestPlaceModelMethods.test_path,
                      TestPlaceModelMethods.path)
        if TestPlaceModelMethods.flag == 1:
            os.remove(TestPlaceModelMethods.path)

    def setUp(self):
        """setup method for the tests in the class"""
        self.model1 = Place()
        self.model1.name = "Holberton"
        self.model1.my_number = 89
        self.model2 = Place()
        self.model2.name = "Betty"
        self.model2.my_number = 98

    def test_save(self):
        """test save Place instance method"""
        self.model2.save()
        self.assertNotIn('updated_at', self.model1.__dict__)
        self.model1.save()
        self.assertIn('updated_at', self.model1.__dict__)
        self.assertIs(type(self.model1.updated_at), datetime)
        self.assertIs(type(self.model1.created_at), datetime)

    def test_to_dict(self):
        """test to_dict Place instance method"""
        self.model1.save()
        self.model1_json = self.model1.to_dict()
        self.assertIs(type(self.model1_json['my_number']), int)
        self.assertEqual(self.model1_json['my_number'], 89)
        self.assertIs(type(self.model1_json['name']), str)
        self.assertEqual(self.model1_json['name'], "Holberton")
        self.assertIs(type(self.model1_json['__class__']), str)
        self.assertEqual(self.model1_json['__class__'], "Place")
        self.assertIs(type(self.model1_json['created_at']), str)
        self.assertIs(type(self.model1_json['updated_at']), str)
        self.assertIs(type(self.model1_json['id']), str)

    def test_json(self):
        """test formatting in the json file"""
        self.model1.save()
        with open(TestPlaceModelMethods.path) as file:
            self.assertIs(os.path.exists(TestPlaceModelMethods.path), True)
            self.json_dict = json.load(file)
            for k, v in self.json_dict.items():
                for key, value in v.items():
                    if key == "created_at":
                        self.assertIs(type(value), str)
                    elif key == "updated_at":
                        self.assertIs(type(value), str)


if __name__ == '__main__':
    unittest.main()
