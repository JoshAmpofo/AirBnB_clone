#!/usr/bin/python3
"""Defines Review module for AirBnB clone"""

from models.base_model import BaseModel


class Review(BaseModel):
    """defines and implements attibutes for place review objects

    Args:
        place_id (str): id of place
        user_id (str): user id
        text (str): review message
    """
    place_id = ""
    user_id = ""
    text = ""
