#!/usr/bin/python3
"""
Unittest for base_model
"""
import unittest
import os
from models.base_model import BaseModel
from models.state import State
import pep8


class Test_State(unittest.TestCase):
    """
    Test class State
    """
    def test_docstring(self):
        """check that docstring exist"""
        self.assertTrue(len(State.__doc__) > 1)
        self.assertTrue(len(State.__init__.__doc__) > 1)
        self.assertTrue(len(State.__str__.__doc__) > 1)
        self.assertTrue(len(State.save.__doc__) > 1)
        self.assertTrue(len(State.to_dict.__doc__) > 1)

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
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
        s0 = State(12)
        self.assertEqual(type(s0).__name__, "State")
        self.assertFalse(hasattr(s0, "12"))

    def test_init_kwarg(self):
        """pass in kwargs to instance"""
        s00 = State(name="Tehe")
        self.assertEqual(type(s00).__name__, "State")
        self.assertTrue(hasattr(s00, "name"))
        self.assertFalse(hasattr(s00, "id"))
        self.assertFalse(hasattr(s00, "created_at"))
        self.assertFalse(hasattr(s00, "updated_at"))
        self.assertTrue(hasattr(s00, "__class__"))

    def test_before_todict(self):
        """test instances before method todict conversion"""
        s1 = State()
        s1_dict = s1.__dict__
        self.assertEqual(type(s1).__name__, "State")
        self.assertTrue(hasattr(s1, '__class__'))
        self.assertEqual(str(s1.__class__),
                         "<class 'models.state.State'>")
        self.assertTrue(type(s1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(s1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(s1_dict['id']), 'str')

    def test_after_todict(self):
        """test instances after method to_dict conversion"""
        my_model = State()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, State)
        self.assertEqual(type(my_model).__name__, "State")
        self.assertEqual(test_dict['__class__'], "State")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')

    def test_str_method(self):
        """test that each method is printing accurately"""
        s3 = State()
        s3printed = s3.__str__()
        self.assertEqual(s3printed,
                         "[State] ({}) {}".format(s3.id, s3.__dict__))

    def test_subclass(self):
        """test subclass"""
        s89 = State()
        self.assertTrue(isinstance(s89, BaseModel))
        self.assertTrue(isinstance(s89, State))

    def test_characteristics(self):
        """test various characteristics of instance"""
        s99 = State()
        self.assertFalse(callable(s99))

    def test_hasattribute(self):
        """test that instance of Base have been correctly made"""
        s2 = State()
        s2.name = "MA"
        self.assertTrue(hasattr(s2, "created_at"))
        self.assertTrue(hasattr(s2, "updated_at"))
        self.assertTrue(hasattr(s2, "id"))
        self.assertTrue(hasattr(s2, "name"))
