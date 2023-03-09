#!/usr/bin/python3
"""
Define and implement User attributes for user side console application"""

from models.base_model import BaseModel


class User(BaseModel):
    """Define User attributes

    Args:
        email (str): user email
        password (str): user security key
        first_name (str): first name of user
        last_name (str): last name of user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
