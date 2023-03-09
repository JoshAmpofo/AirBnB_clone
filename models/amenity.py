#!/usr/bin/python3
"""Defines Amenity attributes for AirBnB clone"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """define and implement attributes for amenities objects

    Arg:
        name (str): name of available amenities
    """
    name = ""
