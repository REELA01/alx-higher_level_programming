#!/usr/bin/python3
"""
Multiply 2 matricies using numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multipication of 2mat
    Args:
        m_a: first mat
        m_b: second mat
    Returns:
        return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)
