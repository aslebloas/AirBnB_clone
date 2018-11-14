#!/usr/bin/python3
"""Module testing file_storage module"""
import os
import unittest
from models.base_model import BaseModel
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
        # if file exist, make a copy of it and remove it
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
        if (TestFileStorageInit.flag == 1 and
            os.path.exists(TestFileStorageInit.path) is True):
            os.remove(TestFileStorageInit.path)

    def test_init(self):
        self.assertIs(
            type(TestFileStorageInit.storage._FileStorage__objects), dict)
        self.assertEqual(TestFileStorageInit.storage._FileStorage__objects, {})

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
            if os.path.exists(TestFileStorageReload.test_path):
                os.remove(TestFileStorageReload.test_path)
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
        if (TestFileStorageReload.flag == 1 and
            os.path.exists(TestFileStorageInit.path) is True):
            os.remove(TestFileStorageReload.path)

    def test_reload(self):
        """Test if the reload function works"""
        self.all_objs = storage.all()
        self.assertEqual(len(self.all_objs), 0)

if __name__ == "__main__":
    unittest.main()
