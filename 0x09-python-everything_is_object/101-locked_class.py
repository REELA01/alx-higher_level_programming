#!/usr/bin/python3
"""Module  of loced calss"""


class LockedClass():
    """class prevent dynamic attributes creation"""
    __slots__ = ['first_name']
