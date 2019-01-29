#!/usr/bin/python3
"""
Unittest for base_model
"""
import unittest
import os
from models.base_model import BaseModel
from models.place import Place
import pep8


class Test_Place(unittest.TestCase):
    """
    Test class Place
    """
    def test_docstring(self):
        """check that docstring exist"""
        self.assertTrue(len(Place.__doc__) > 1)
        self.assertTrue(len(Place.__init__.__doc__) > 1)
        self.assertTrue(len(Place.__str__.__doc__) > 1)
        self.assertTrue(len(Place.save.__doc__) > 1)
        self.assertTrue(len(Place.to_dict.__doc__) > 1)

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
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
        pl0 = Place(12)
        self.assertEqual(type(pl0).__name__, "Place")
        self.assertFalse(hasattr(pl0, "12"))

    def test_init_kwarg(self):
        """pass in kwargs to instance"""
        pl00 = Place(name="Tehe")
        self.assertEqual(type(pl00).__name__, "Place")
        self.assertTrue(hasattr(pl00, "name"))
        self.assertFalse(hasattr(pl00, "id"))
        self.assertFalse(hasattr(pl00, "created_at"))
        self.assertFalse(hasattr(pl00, "updated_at"))
        self.assertTrue(hasattr(pl00, "__class__"))

    def test_before_todict(self):
        """test instances before method todict conversion"""
        pl1 = Place()
        pl1_dict = pl1.__dict__
        self.assertEqual(type(pl1).__name__, "Place")
        self.assertTrue(hasattr(pl1, '__class__'))
        self.assertEqual(str(pl1.__class__),
                         "<class 'models.place.Place'>")
        self.assertTrue(type(pl1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(pl1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(pl1_dict['id']), 'str')

    def test_after_todict(self):
        """test instances after method to_dict conversion"""
        my_model = Place()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, Place)
        self.assertEqual(type(my_model).__name__, "Place")
        self.assertEqual(test_dict['__class__'], "Place")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')

    def test_str_method(self):
        """test that each method is printing accurately"""
        pl3 = Place()
        pl3printed = pl3.__str__()
        self.assertEqual(pl3printed,
                         "[Place] ({}) {}".format(pl3.id, pl3.__dict__))

    def test_subclass(self):
        """test succlass"""
        pl89 = Place()
        self.assertTrue(isinstance(pl89, BaseModel))
        self.assertTrue(isinstance(pl89, Place))

    def test_characteristics(self):
        """test various characteristics of instance"""
        pl99 = Place()
        self.assertFalse(callable(pl99))

    def test_hasattribute(self):
        """test that instance of Base have been correctly made"""
        pl2 = Place()
        self.assertTrue(hasattr(pl2, "created_at"))
        self.assertTrue(hasattr(pl2, "updated_at"))
        self.assertTrue(hasattr(pl2, "id"))
        self.assertTrue(hasattr(pl2, "city_id"))
        self.assertTrue(hasattr(pl2, "user_id"))
        self.assertTrue(hasattr(pl2, "name"))
        self.assertTrue(hasattr(pl2, "description"))
        self.assertTrue(hasattr(pl2, "number_rooms"))
        self.assertTrue(hasattr(pl2, "number_bathrooms"))
        self.assertTrue(hasattr(pl2, "max_guest"))
        self.assertTrue(hasattr(pl2, "price_by_night"))
        self.assertTrue(hasattr(pl2, "latitude"))
        self.assertTrue(hasattr(pl2, "longitude"))
        self.assertTrue(hasattr(pl2, "amenity_ids"))
