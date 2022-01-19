#!/usr/bin/python3
"""Class MagicClas"""
import math


class MagicClass:
    """Defines MagicClas"""
    def __init__(self, radius=0):
        """Iniitializes Dataa"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Get area."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Get Circumference."""
        return (2 * math.pi * self.__radius)
