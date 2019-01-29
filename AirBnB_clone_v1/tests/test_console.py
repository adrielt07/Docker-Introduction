#!/usr/bin/python3
"""
Tests for the console
"""
import pep8
import os
from console import HBNBCommand
import unittest
from io import StringIO
import sys
from unittest.mock import create_autospec


class Test_Console(unittest.TestCase):
    """
    test class Console
    """
    def test_docstring(self):
        """check that docstring exist"""
        self.assertTrue(len(HBNBCommand.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.__init__.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_quit.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_EOF.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.emptyline.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_create.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_show.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_all.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_destroy.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_update.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.default.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_count.__doc__) > 1)
