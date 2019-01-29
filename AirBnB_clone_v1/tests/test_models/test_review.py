#!/usr/bin/python3
"""
Unittest for base_model
"""
import unittest
import os
from models.base_model import BaseModel
from models.review import Review
import pep8


class Test_Review(unittest.TestCase):
    """
    Test class Review
    """
    def test_docstring(self):
        """check that docstring exist"""
        self.assertTrue(len(Review.__doc__) > 1)
        self.assertTrue(len(Review.__init__.__doc__) > 1)
        self.assertTrue(len(Review.__str__.__doc__) > 1)
        self.assertTrue(len(Review.save.__doc__) > 1)
        self.assertTrue(len(Review.to_dict.__doc__) > 1)

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
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
        rev0 = Review(12)
        self.assertEqual(type(rev0).__name__, "Review")
        self.assertFalse(hasattr(rev0, "12"))

    def test_init_kwarg(self):
        """pass in kwargs to instance"""
        rev00 = Review(name="Tehe")
        self.assertEqual(type(rev00).__name__, "Review")
        self.assertTrue(hasattr(rev00, "name"))
        self.assertFalse(hasattr(rev00, "id"))
        self.assertFalse(hasattr(rev00, "created_at"))
        self.assertFalse(hasattr(rev00, "updated_at"))
        self.assertTrue(hasattr(rev00, "__class__"))

    def test_before_todict(self):
        """test instances before method todict conversion"""
        rev1 = Review()
        rev1_dict = rev1.__dict__
        self.assertEqual(type(rev1).__name__, "Review")
        self.assertTrue(hasattr(rev1, '__class__'))
        self.assertEqual(str(rev1.__class__),
                         "<class 'models.review.Review'>")
        self.assertTrue(type(rev1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(rev1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(rev1_dict['id']), 'str')

    def test_after_todict(self):
        """test instances after method to_dict conversion"""
        my_model = Review()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, Review)
        self.assertEqual(type(my_model).__name__, "Review")
        self.assertEqual(test_dict['__class__'], "Review")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')

    def test_str_method(self):
        """test that each method is printing accurately"""
        rev3 = Review()
        rev3printed = rev3.__str__()
        self.assertEqual(rev3printed,
                         "[Review] ({}) {}".format(rev3.id, rev3.__dict__))

    def test_subclass(self):
        """test succlass"""
        rev89 = Review()
        self.assertTrue(isinstance(rev89, BaseModel))
        self.assertTrue(isinstance(rev89, Review))

    def test_characteristics(self):
        """test various characteristics of instance"""
        rev99 = Review()
        self.assertFalse(callable(rev99))

    def test_hasattribute(self):
        """test that instance of Base have been correctly made"""
        rev2 = Review()
        self.assertTrue(hasattr(rev2, "created_at"))
        self.assertTrue(hasattr(rev2, "updated_at"))
        self.assertTrue(hasattr(rev2, "id"))
        self.assertTrue(hasattr(rev2, "place_id"))
        self.assertTrue(hasattr(rev2, "user_id"))
        self.assertTrue(hasattr(rev2, "text"))
