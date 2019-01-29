#!/usr/bin/python3
"""Module: user - Class: User"""
import models


class User(models.BaseModel):
    """
    Inherting from BaseModel
    Setting class attribute
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
