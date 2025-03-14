"""
Lower-upper (LU) decomposition factors a matrix as a product of a lower
triangular matrix and an upper triangular matrix. A square matrix has an LU
decomposition under the following conditions:

    - If the matrix is invertible, then it has an LU decomposition if and only
      if all of its leading principal minors are non-zero (see
      https://en.wikipedia.org/wiki/Minor_(linear_algebra) for an explanation of
      leading principal minors of a matrix).
    - If the matrix is singular (i.e., not invertible) and it has a rank of k
      (i.e., it has k linearly independent columns), then it has an LU
      decomposition if its first k leading principal minors are non-zero.

This algorithm will simply attempt to perform LU decomposition on any square
matrix and raise an error if no such decomposition exists.

Reference: https://en.wikipedia.org/wiki/LU_decomposition
"""

from __future__ import annotations

import numpy as np


def lower_upper_decomposition(table: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Perform LU decomposition on a given matrix and raise an error if the matrix
    isn't square or if no such decomposition exists

    >>> matrix = np.array([[2, -2, 1], [0, 1, 2], [5, 3, 1]])
    >>> lower_mat, upper_mat = lower_upper_decomposition(matrix)
    >>> lower_mat
    array([[1. , 0. , 0. ],
           [0. , 1. , 0. ],
           [2.5, 8. , 1. ]])
    >>> upper_mat
    array([[  2. ,  -2. ,   1. ],
           [  0. ,   1. ,   2. ],
           [  0. ,   0. , -17.5]])

    >>> matrix = np.array([[4, 3], [6, 3]])
    >>> lower_mat, upper_mat = lower_upper_decomposition(matrix)
    >>> lower_mat
    array([[1. , 0. ],
           [1.5, 1. ]])
    >>> upper_mat
    array([[ 4. ,  3. ],
           [ 0. , -1.5]])

    >>> # Matrix is not square
    >>> matrix = np.array([[2, -2, 1], [0, 1, 2]])
    >>> lower_mat, upper_mat = lower_upper_decomposition(matrix)
    Traceback (most recent call last):
        ...
    ValueError: 'table' has to be of square shaped array but got a 2x3 array:
    [[ 2 -2  1]
     [ 0  1  2]]

    >>> # Matrix is invertible, but its first leading principal minor is 0
    >>> matrix = np.array([[0, 1], [1, 0]])
    >>> lower_mat, upper_mat = lower_upper_decomposition(matrix)
    Traceback (most recent call last):
    ...
    ArithmeticError: No LU decomposition exists

    >>> # Matrix is singular, but its first leading principal minor is 1
    >>> matrix = np.array([[1, 0], [1, 0]])
    >>> lower_mat, upper_mat = lower_upper_decomposition(matrix)
    >>> lower_mat
    array([[1., 0.],
           [1., 1.]])
    >>> upper_mat
    array([[1., 0.],
           [0., 0.]])

    >>> # Matrix is singular, but its first leading principal minor is 0
    >>> matrix = np.array([[0, 1], [0, 1]])
    >>> lower_mat, upper_mat = lower_upper_decomposition(matrix)
    Traceback (most recent call last):
    ...
    ArithmeticError: No LU decomposition exists
    """
    # Ensure that table is a square array
    rows, columns = table.shape
    if rows != columns:
        msg = (
            "'table' has to be of square shaped array but got a "
            f"{rows}x{columns} array:\n{table}"
        )
        raise ValueError(msg)

    lower = np.eye(rows)  # Allocate lower as an identity matrix
    upper = np.zeros((rows, columns))

    for i in range(columns):
        for j in range(i, columns):
            total = np.dot(lower[i, :i], upper[:i, j])
            upper[i][j] = table[i][j] - total

        for j in range(i + 1, columns):
            total = np.dot(lower[j, :i], upper[:i, i])
            if upper[i][i] == 0:
                raise ArithmeticError("No LU decomposition exists")
            lower[j][i] = (table[j][i] - total) / upper[i][i]

    return lower, upper


if __name__ == "__main__":
    import doctest

    doctest.testmod()
