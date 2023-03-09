#!/usr/bin/python3
"""Defines Place attributes for AirBnB clone"""

from models.base_model import BaseModel


class Place(BaseModel):
    """define and implement attributes for place objects

    Args:
        city_id (str): id of city
        user_id (string): user id
        name (str): name of place
        description (str): commentary on place
        number_rooms (int): number of rooms available in place
        number_bathrooms (int): number of bathroom available in place
        max_guest (int): max guests allowed in place
        price_by_night (int): price of per night stay
        latitude (float): map coordinates of place
        longitude (float): map coordinates of place
        amenity_ids (list): list of available amenities at place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
