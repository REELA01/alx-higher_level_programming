#!/usr/bin/python3
"""matrix_mul function"""


def matrix_mul(m_a, m_b):
    """multiplies two mat
    Args:
        m_a: first mat
        m_b: second mat
    Returns:
        matrix: the result of multiplication
    Raises:
        TypeError: if matiatixes are not lisits
        TypeError: if matrixes are not lists of lists
        ValueError: if m_a or m_b are empty
        TypeError: if m_a or m_b not int/float
        TypeError: if m_a or m_b are not rectangular
        ValueError: if m_a or m_b can not be multiplied
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    m_a_empty = False
    m_b_empty = False
    m_a_notrec = False
    m_b_notrec = False
    m_a_notnum = False
    m_b_notnum = False
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            m_a_notrec = True
        for n in row:
            if not isinstance(n, (int, float)):
                m_a_notnum = True

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            m_b_notrec = True
        for n in row:
            if not isinstance(n, (int, float)):
                m_b_notnum = True

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    if m_a_notnum:
        raise TypeError("m_a should contain only integers or floats")
    if m_a_notrec:
        raise TypeError("each row of m_a must should be of the same size")
    if m_b_notnum:
        raise TypeError("m_b should contain only integers or floats")
    if m_b_notrec:
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    r = [[] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            c = 0
            for k in range(len(m_b)):
                c += m_a[i][k] * m_b[k][j]
            r[i].append(c)
    return r

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
