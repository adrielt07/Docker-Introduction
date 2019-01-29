#!/usr/bin/python3
"""
Unittest for base_model
"""
import unittest
import sys
from io import StringIO
from models.base_model import BaseModel
import pep8


class Test_BaseModel(unittest.TestCase):
    """
    Test class BaseModel
    """
    def test_docstring(self):
        """check that docstring exist"""
        self.assertTrue(len(BaseModel.__doc__) > 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "pep8")

    def setUp(self):
        """set up before every test method"""
        pass

    def tearDown(self):
        """remove file.json after the finish of each test method"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_init_arg(self):
        """pass in arg to new instance"""
        b0 = BaseModel(12)
        self.assertEqual(type(b0).__name__, "BaseModel")
        self.assertFalse(hasattr(b0, "12"))

    def test_init_kwarg(self):
        """pass in kwargs to instance"""
        b00 = BaseModel(name="Tehe")
        self.assertEqual(type(b00).__name__, "BaseModel")
        self.assertTrue(hasattr(b00, "name"))
        self.assertFalse(hasattr(b00, "id"))
        self.assertFalse(hasattr(b00, "created_at"))
        self.assertFalse(hasattr(b00, "updated_at"))
        self.assertTrue(hasattr(b00, "__class__"))

    def test_datetime(self):
        """test datetime for created_at and updated_at is the same"""
        mom = BaseModel()
        self.assertEqual(mom.created_at, mom.updated_at)
        mom_dict = mom.to_dict()
        self.assertEqual(mom_dict['created_at'], mom_dict['updated_at'])
        mom.save()
        mom_dict = mom.to_dict()
        self.assertNotEqual(mom_dict['created_at'], mom_dict['updated_at'])

    def test_before_todict(self):
        """test instances before method todict conversion"""
        b1 = BaseModel()
        b1_dict = b1.__dict__
        self.assertEqual(type(b1).__name__, "BaseModel")
        self.assertTrue(hasattr(b1, '__class__'))
        self.assertEqual(str(b1.__class__),
                         "<class 'models.base_model.BaseModel'>")
        self.assertTrue(type(b1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['id']), 'str')

    def test_after_todict(self):
        """test instances after method to_dict conversion"""
        my_model = BaseModel()
        new_model = BaseModel()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, BaseModel)
        self.assertEqual(type(my_model).__name__, "BaseModel")
        self.assertEqual(test_dict['__class__'], "BaseModel")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def test_str_method(self):
        """test that each method is printing accurately"""
        b3 = BaseModel()
        b3printed = b3.__str__()
        self.assertEqual(b3printed,
                         "[BaseModel] ({}) {}".format(b3.id, b3.__dict__))

    def test_hasattribute(self):
        """test that instance of Base have been correctly made"""
        b2 = BaseModel()
        self.assertTrue(hasattr(b2, "__init__"))
        self.assertTrue(hasattr(b2, "created_at"))
        self.assertTrue(hasattr(b2, "updated_at"))
        self.assertTrue(hasattr(b2, "id"))
