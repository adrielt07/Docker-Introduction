#!/usr/bin/python3
"""
Executes storage when module is called
"""
from models.engine import file_storage
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State


storage = file_storage.FileStorage()
storage.reload()

if __name__ != '__main__':
    def error_check(list_arg=[], n=0):
        """Check for common error messages for all methods"""
        check_class = ['BaseModel', 'User', 'State',
                       'City', 'Amenity', 'Place', 'Review']
        try:
            class_name = "{}".format(list_arg[0])
        except IndexError:
            if len(list_arg) == 0:
                print("** class name missing **")
                return 0
        if class_name not in check_class:
            print("** class doesn't exist **")
            return 0

        if n == 0:
            try:
                key = "{}.{}".format(list_arg[0], list_arg[1])
                return key
            except IndexError:
                if len(list_arg) == 1:
                    print("** instance id missing **")
                    return 0
