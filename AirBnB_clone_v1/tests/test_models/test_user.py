#!/usr/bin/python3
"""
Unittest for base_model
"""
import unittest
import os
from models.base_model import BaseModel
from models.user import User
import pep8


class Test_User(unittest.TestCase):
    """
    Test class User
    """
    def test_docstring(self):
        """check that docstring exist"""
        self.assertTrue(len(User.__doc__) > 1)
        self.assertTrue(len(User.__init__.__doc__) > 1)
        self.assertTrue(len(User.__str__.__doc__) > 1)
        self.assertTrue(len(User.save.__doc__) > 1)
        self.assertTrue(len(User.to_dict.__doc__) > 1)

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
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
        user0 = User(12)
        self.assertEqual(type(user0).__name__, "User")
        self.assertFalse(hasattr(user0, "12"))

    def test_init_kwarg(self):
        """pass in kwargs to instance"""
        user00 = User(name="Tehe")
        self.assertEqual(type(user00).__name__, "User")
        self.assertTrue(hasattr(user00, "name"))
        self.assertFalse(hasattr(user00, "id"))
        self.assertFalse(hasattr(user00, "created_at"))
        self.assertFalse(hasattr(user00, "updated_at"))
        self.assertTrue(hasattr(user00, "__class__"))

    def test_before_todict(self):
        """test instances before method todict conversion"""
        user1 = User()
        user1_dict = user1.__dict__
        self.assertEqual(type(user1).__name__, "User")
        self.assertTrue(hasattr(user1, '__class__'))
        self.assertEqual(str(user1.__class__),
                         "<class 'models.user.User'>")
        self.assertTrue(type(user1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(user1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(user1_dict['id']), 'str')

    def test_after_todict(self):
        """test instances after method to_dict conversion"""
        my_model = User()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, User)
        self.assertEqual(type(my_model).__name__, "User")
        self.assertEqual(test_dict['__class__'], "User")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')

    def test_str_method(self):
        """test that each method is printing accurately"""
        user3 = User()
        user3printed = user3.__str__()
        self.assertEqual(user3printed,
                         "[User] ({}) {}".format(user3.id, user3.__dict__))

    def test_subclass(self):
        """test subclass"""
        user89 = User()
        self.assertTrue(isinstance(user89, BaseModel))
        self.assertTrue(isinstance(user89, User))

    def test_characteristics(self):
        """test various characteristics of instance"""
        user99 = User()
        self.assertFalse(callable(user99))

    def test_hasattribute(self):
        """test that instance of Base have been correctly made"""
        user2 = User()
        self.assertTrue(hasattr(user2, "created_at"))
        self.assertTrue(hasattr(user2, "updated_at"))
        self.assertTrue(hasattr(user2, "id"))
        self.assertTrue(hasattr(user2, "email"))
        self.assertTrue(hasattr(user2, "password"))
        self.assertTrue(hasattr(user2, "first_name"))
        self.assertTrue(hasattr(user2, "last_name"))
