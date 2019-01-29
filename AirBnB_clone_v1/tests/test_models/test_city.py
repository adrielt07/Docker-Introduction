#!/usr/bin/python3
"""
Unittest for base_model
"""
import unittest
import os
from models.base_model import BaseModel
from models.city import City
import pep8


class Test_City(unittest.TestCase):
    """
    Test class City
    """
    def test_docstring(self):
        """check that docstring exist"""
        self.assertTrue(len(City.__doc__) > 1)
        self.assertTrue(len(City.__init__.__doc__) > 1)
        self.assertTrue(len(City.__str__.__doc__) > 1)
        self.assertTrue(len(City.save.__doc__) > 1)
        self.assertTrue(len(City.to_dict.__doc__) > 1)

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
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
        c0 = City(12)
        self.assertEqual(type(c0).__name__, "City")
        self.assertFalse(hasattr(c0, "12"))

    def test_init_kwarg(self):
        """pass in kwargs to instance"""
        c00 = City(name="Tehe")
        self.assertEqual(type(c00).__name__, "City")
        self.assertTrue(hasattr(c00, "name"))
        self.assertFalse(hasattr(c00, "id"))
        self.assertFalse(hasattr(c00, "created_at"))
        self.assertFalse(hasattr(c00, "updated_at"))
        self.assertTrue(hasattr(c00, "__class__"))

    def test_before_todict(self):
        """test instances before method todict conversion"""
        c1 = City()
        c1_dict = c1.__dict__
        self.assertEqual(type(c1).__name__, "City")
        self.assertTrue(hasattr(c1, '__class__'))
        self.assertEqual(str(c1.__class__),
                         "<class 'models.city.City'>")
        self.assertTrue(type(c1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(c1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(c1_dict['id']), 'str')

    def test_after_todict(self):
        """test instances after method to_dict conversion"""
        my_model = City()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, City)
        self.assertEqual(type(my_model).__name__, "City")
        self.assertEqual(test_dict['__class__'], "City")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')

    def test_str_method(self):
        """test that each method is printing accurately"""
        c3 = City()
        c3printed = c3.__str__()
        self.assertEqual(c3printed,
                         "[City] ({}) {}".format(c3.id, c3.__dict__))

    def test_subclass(self):
        """test succlass"""
        c89 = City()
        self.assertTrue(isinstance(c89, BaseModel))
        self.assertTrue(isinstance(c89, City))

    def test_characteristics(self):
        """test various characteristics of instance"""
        c99 = City()
        self.assertFalse(callable(c99))

    def test_hasattribute(self):
        """test that instance of Base have been correctly made"""
        c2 = City()
        c2.state_id = 'MA'
        c2.name = "Whitey Bulger"
        self.assertTrue(hasattr(c2, "created_at"))
        self.assertTrue(hasattr(c2, "updated_at"))
        self.assertTrue(hasattr(c2, "id"))
        self.assertTrue(hasattr(c2, "state_id"))
        self.assertTrue(hasattr(c2, "name"))
