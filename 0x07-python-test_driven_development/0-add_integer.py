#!/usr/bin/python3
'''add_integer function
'''


def add_integer(a, b=98):
    '''add tow numbers
    Args:
        a: the first number
        b: the second number
    Returns:
        int: the sum
    '''
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
