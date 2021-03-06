#!/usr/bin/python3
"""Module testing file_storage module"""
import json
import os
import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorageInit(unittest.TestCase):
    """Test for FileStorage instance initialization"""
    path = os.path.abspath("file.json")
    test_path = os.path.abspath("test_file.json")
    flag = 0

    @classmethod
    def setUpClass(cls):
        """Class setup method"""
        cls.storage = FileStorage()
        # if json file exist, make a copy of it and remove it
        if os.path.exists(TestFileStorageInit.path) is True:
            if os.path.exists(TestFileStorageInit.test_path):
                os.remove(TestFileStorageInit.test_path)
            os.rename(TestFileStorageInit.path,
                      TestFileStorageInit.test_path)
        else:
            TestFileStorageInit.flag = 1

    @classmethod
    def tearDownClass(cls):
        """Teardown objects"""
        # remove file at the end of the test and restore copy
        if os.path.exists(TestFileStorageInit.test_path) is True:
            os.rename(TestFileStorageInit.test_path,
                      TestFileStorageInit.path)
        if ((os.path.exists(TestFileStorageInit.path) and
                TestFileStorageInit.flag == 1)):
            os.remove(TestFileStorageInit.path)

    def test_init(self):
        self.assertIs(
            type(TestFileStorageInit.storage._FileStorage__file_path), str)
        self.assertEqual(
            TestFileStorageInit.storage._FileStorage__file_path,
            TestFileStorageInit.path)


class TestFileStorageReload(unittest.TestCase):
    """Test for FileStorage instance initialization"""
    path = os.path.abspath("file.json")
    test_path = os.path.abspath("test_file.json")
    flag = 0

    @classmethod
    def setUpClass(cls):
        """Class setup method"""
        cls.storage = FileStorage()
        # if file exist, make a copy of it and remove it
        if os.path.exists(TestFileStorageReload.path) is True:
            # remove the previous test file
            if os.path.exists(TestFileStorageReload.test_path):
                os.remove(TestFileStorageReload.test_path)
            # copy file to the copy
            os.rename(TestFileStorageReload.path,
                      TestFileStorageReload.test_path)
        else:
            TestFileStorageReload.flag = 1

    @classmethod
    def tearDownClass(cls):
        """Teardown objects"""
        # remove file at the end of the test and restore copy
        if os.path.exists(TestFileStorageReload.test_path) is True:
            os.rename(TestFileStorageReload.test_path,
                      TestFileStorageReload.path)
        if ((TestFileStorageReload.flag == 1 and
             os.path.exists(TestFileStorageInit.path))):
            os.remove(TestFileStorageReload.path)

    def test_reload(self):
        """test reload"""
        self.all_objs = storage.all()
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 98
        my_model.my_float = 2.3

        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Holberton"
        my_user.email = "airbnb@holbertonshool.com"
        my_user.password = "root"

        my_model.save()
        my_user.save()

        self.all_objs = storage.all()
        self.assertTrue(len(self.all_objs) > 0)

        for self.obj_id in self.all_objs.keys():
            self.obj = self.all_objs[self.obj_id]
            self.assertIsNot(type(self.obj), dict)
            self.assertEqual(self.obj_id.split('.')[0],
                             self.obj.__class__.__name__)


class TestFileStorageSave(unittest.TestCase):
    """Test for FileStorage instance initialization"""
    path = os.path.abspath("file.json")
    test_path = os.path.abspath("test_file.json")
    flag = 0

    @classmethod
    def setUpClass(cls):
        """Class setup method"""
        cls.storage = FileStorage()
        # if file exist, make a copy of it and remove it
        if os.path.exists(TestFileStorageSave.path) is True:
            # remove the previous test file
            if os.path.exists(TestFileStorageSave.test_path):
                os.remove(TestFileStorageSave.test_path)
            # copy file to the copy
            os.rename(TestFileStorageSave.path,
                      TestFileStorageSave.test_path)
        else:
            TestFileStorageSave.flag = 1

    @classmethod
    def tearDownClass(cls):
        """Teardown objects"""
        # remove file at the end of the test and restore copy
        if os.path.exists(TestFileStorageSave.test_path) is True:
            os.rename(TestFileStorageSave.test_path,
                      TestFileStorageSave.path)
        if ((TestFileStorageSave.flag == 1 and
             os.path.exists(TestFileStorageInit.path))):
            os.remove(TestFileStorageSave.path)

    def SetUp(self):
        """Set up new object"""
        self.my_model = BaseModel()

    def test_save(self):
        """test save
        Args:
            obj: object to be saved to file
        """
        storage.save()
        with open(TestFileStorageSave.path) as file:
            dictionary = json.load(file)
            for k, v in dictionary.items():
                self.assertIs(type(v), dict)
                self.assertEqual(k.split('.')[0],
                                 v['__class__'])

if __name__ == "__main__":
    unittest.main()
