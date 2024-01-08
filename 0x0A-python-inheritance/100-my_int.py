#!/usr/bin/python3
"""define MyInt class"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, other):
        """reverting == to !="""
        return int(self) != int(other)

    def __ne__(self, other):
        """reverting != to =="""
        return int(self) == int(other)
