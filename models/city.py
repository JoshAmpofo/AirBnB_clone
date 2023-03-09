#!/usr/bin/python3
"""Defines City attributes for AirBnB clone"""

from models.base_model import BaseModel


class City(BaseModel):
    """defines and implements attributes for City objects

    Args:
        state_id (str): id for State in which City can be found
        name (str): name of city
    """
    state_id = ""
    name = ""
