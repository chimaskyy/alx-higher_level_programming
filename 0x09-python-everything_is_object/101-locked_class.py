#!/usr/bin/python3
"""
Locked class
"""

class LockedClass:
    """class definition
    This class takes only one attribute
    Any attempt to assign another attribute
    will raise attribute error
    """
    __slot__ = ('first_name',)

    def __init__(self):
        self.first_name = None