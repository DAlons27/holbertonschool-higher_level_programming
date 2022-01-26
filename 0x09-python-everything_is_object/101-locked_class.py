#!/usr/bin/python3

"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockeClass attributes
    for anything but atributes called 'first_name'.
    """

    __slots__ = ["first_name"]