#!/usr/bin/python3
"""Define State attribute for AirBnB clone"""

from models.base_model import BaseModel


class State(BaseModel):
    """Defines and implements attributes for State objects

    Args:
        name (str): name of state
    """
    name = ""
