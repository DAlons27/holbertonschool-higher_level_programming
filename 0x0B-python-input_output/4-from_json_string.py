#!/usr/bin/python3
"""Returns an object (Python data structure)"""


import json


def from_json_string(my_str):
    """Return the object represented my my_str.
    Args:
        - my_str: JSON string representation
    Returns: corresponding object
    """

    return json.loads(my_str)
