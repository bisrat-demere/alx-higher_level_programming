#!/usr/bin/python3
"""
student class
"""


class Student:

    """
    Represent Student Object
    """
    def __init__(self, first_name, last_name, age):

        """
        initialization
        Args:
            first_name: first_name
            last_name: last_name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        """
        Convert to json
        """
        return self.__dict__
