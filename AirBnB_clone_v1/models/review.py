#!/usr/bin/python3
"""Module: review - Class: Review"""
import models


class Review(models.BaseModel):
    """
    Inheritive from BaseModel
    class Review
    """
    place_id = ""
    user_id = ""
    text = ""
