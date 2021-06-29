#!/usr/bin/python3
"""This file contains the class User that inherits from BaseModel."""
import models


class User(models.base_model.BaseModel):
    """Public class attributes:"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
