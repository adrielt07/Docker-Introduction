#!/usr/bin/python3
"""
Unittest for base_model
"""
import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity
import pep8


class Test_Amenity(unittest.TestCase):
    """
    Test class Amenity
    """
    def test_docstring(self):
        """check that docstring exist"""
        self.assertTrue(len(Amenity.__doc__) > 1)
        self.assertTrue(len(Amenity.__init__.__doc__) > 1)
        self.assertTrue(len(Amenity.__str__.__doc__) > 1)
        self.assertTrue(len(Amenity.save.__doc__) > 1)
        self.assertTrue(len(Amenity.to_dict.__doc__) > 1)

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "pep8")

    def setUp(self):
        """
        redirect stdout of the output for functions using print
        """
        pass

    def tearDown(self):
        """
        re-establish the stdout back to normal after setUp
        """
        try:
            os.remove("file.json")
        except:
            pass

    def test_init_arg(self):
        """pass in arg to new instance"""
        a0 = Amenity(12)
        self.assertEqual(type(a0).__name__, "Amenity")
        self.assertFalse(hasattr(a0, "12"))

    def test_init_kwarg(self):
        """pass in kwargs to instance"""
        a00 = Amenity(name="Tehe")
        self.assertEqual(type(a00).__name__, "Amenity")
        self.assertTrue(hasattr(a00, "name"))
        self.assertFalse(hasattr(a00, "id"))
        self.assertFalse(hasattr(a00, "created_at"))
        self.assertFalse(hasattr(a00, "updated_at"))
        self.assertTrue(hasattr(a00, "__class__"))

    def test_before_todict(self):
        """test instances before method todict conversion"""
        a1 = Amenity()
        a1_dict = a1.__dict__
        self.assertEqual(type(a1).__name__, "Amenity")
        self.assertTrue(hasattr(a1, '__class__'))
        self.assertEqual(str(a1.__class__),
                         "<class 'models.amenity.Amenity'>")
        self.assertTrue(type(a1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(a1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(a1_dict['id']), 'str')

    def test_after_todict(self):
        """test instances after method to_dict conversion"""
        my_model = Amenity()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, Amenity)
        self.assertEqual(type(my_model).__name__, "Amenity")
        self.assertEqual(test_dict['__class__'], "Amenity")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')

    def test_str_method(self):
        """test that each method is printing accurately"""
        a3 = Amenity()
        a3printed = a3.__str__()
        self.assertEqual(a3printed,
                         "[Amenity] ({}) {}".format(a3.id, a3.__dict__))

    def test_subclass(self):
        """test succlass"""
        a89 = Amenity()
        self.assertTrue(isinstance(a89, BaseModel))
        self.assertTrue(isinstance(a89, Amenity))

    def test_characteristics(self):
        """test various characteristics of instance"""
        a99 = Amenity()
        self.assertFalse(callable(a99))

    def test_hasattribute(self):
        """test that instance of Base have been correctly made"""
        a2 = Amenity()
        a2.name = "Indoor Fireplace"
        self.assertTrue(hasattr(a2, "created_at"))
        self.assertTrue(hasattr(a2, "updated_at"))
        self.assertTrue(hasattr(a2, "id"))
        self.assertTrue(hasattr(a2, "name"))
