#!/usr/bin/python3
"""File Storage Test"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
import unittest
import pep8
import os
import json


class Test_FileStorage(unittest.TestCase):
    """
    Test Class FileStorage
    """

    def test_docstring(self):
        """check that docstring exist"""
        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "pep8")

    def setUp(self):
        """set up"""
        pass

    def tearDown(self):
        """tear down"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_all(self):
        """Method for all"""
        f0 = FileStorage()
        f_in_objects = f0.all()
        self.assertTrue(type(f_in_objects), dict)

    def test_new(self):
        """Test method for new"""
        """
        Tests method: new (saves new object into dictionary)
        """
        f00 = FileStorage()
        obj_inst = f00.all()
        u1 = User()
        u1.id = 000
        u1.name = "Hehehe"
        f00.new(u1)
        key = u1.__class__.__name__ + "." + str(u1.id)
        self.assertIsNotNone(obj_inst[key])

    def test_save_method(self):
        """Test save method"""
        b1 = BaseModel()
        b1.save()
        self.assertTrue(os.path.isfile("file.json"))
        with open("file.json", "r", encoding="utf-8") as f:
            n = json.load(f)
            self.assertEqual(type(n), dict)
            for k, v in n.items():
                self.assertTrue(type(v), dict)
                self.assertTrue(len(v) > 0)
                d = BaseModel(**v)
        self.assertIsInstance(d, BaseModel)
        self.assertTrue(type(d.__dict__), dict)
        self.assertTrue(d.id, b1.id)
        self.assertTrue(d.__class__, b1.__class__)
#        for k, v in b1.__dict__.items():
#            self.assertTrue(k in d.__dict__)
#            if k is 'created_at' or 'updated_at':
#                setattr(d, k, datetime.isoformat(d.updated_at))
#                setattr(b1, k, datetime.isoformat(b1.updated_at))
#        self.assertEqual(b1.__dict__["updated_at"],
#                         d.__dict__["updated_at"])
#                self.assertEqual(d.__dict__[k], b1.__dict__[k])
#                    else:
#                        self.assertEqual(d.__dict__[k], b1.__dict__[k])

    def test_reload(self):
        """Test reload method"""
        f3 = FileStorage()
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as wee:
            for arg in wee:
                self.assertEqual(arg, "{}")
        self.assertIs(f3.reload(), None)

    def test_json_error(self):
        """Raise errors related to JSON conversion"""
        with self.assertRaises(AttributeError):
            FileStorage.__objects
            FileStorage.__File_Path
