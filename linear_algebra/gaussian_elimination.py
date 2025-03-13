"""
| Gaussian elimination method for solving a system of linear equations.
| Gaussian elimination - https://en.wikipedia.org/wiki/Gaussian_elimination
"""

import numpy as np
from numpy import float64
from numpy.typing import NDArray


def retroactive_resolution(
    coefficients: NDArray[float64], vector: NDArray[float64]
) -> NDArray[float64]:
    """
    This function performs a retroactive linear system resolution
    for triangular matrix

    Examples:
        1.
            * 2x1 + 2x2 - 1x3 = 5
            * 0x1 - 2x2 - 1x3 = -7
            * 0x1 + 0x2 + 5x3 = 15
        2.
            * 2x1 + 2x2 = -1
            * 0x1 - 2x2 = -1

    >>> gaussian_elimination([[2, 2, -1], [0, -2, -1], [0, 0, 5]], [[5], [-7], [15]])
    array([[2.],
           [2.],
           [3.]])
    >>> gaussian_elimination([[2, 2], [0, -2]], [[-1], [-1]])
    array([[-1. ],
           [ 0.5]])
    """
    rows, _ = coefficients.shape
    x = np.empty((rows, 1), dtype=float64)
    for row in range(rows - 1, -1, -1):
        total = np.dot(coefficients[row, row + 1:], x[row + 1:, 0])
        x[row, 0] = (vector[row, 0] - total) / coefficients[row, row]

    return x


def gaussian_elimination(
    coefficients: NDArray[float64], vector: NDArray[float64]
) -> NDArray[float64]:
    """
    This function performs Gaussian elimination method

    Examples:
        1.
            * 1x1 - 4x2 - 2x3 = -2
            * 5x1 + 2x2 - 2x3 = -3
            * 1x1 - 1x2 + 0x3 = 4
        2.
            * 1x1 + 2x2 = 5
            * 5x1 + 2x2 = 5

    >>> gaussian_elimination([[1, -4, -2], [5, 2, -2], [1, -1, 0]], [[-2], [-3], [4]])
    array([[ 2.3 ],
           [-1.7 ],
           [ 5.55]])
    >>> gaussian_elimination([[1, 2], [5, 2]], [[5], [5]])
    array([[0. ],
           [2.5]])
    """
    # coefficients must to be a square matrix so we need to check first
    rows, columns = coefficients.shape
    if rows != columns:
        return np.array([], dtype=float64)

    # augmented matrix
    augmented_mat = np.hstack((coefficients, vector)).astype(float64)

    # scale the matrix leaving it triangular
    for row in range(rows - 1):
        pivot = augmented_mat[row, row]
        augmented_mat[row+1:, :] -= (augmented_mat[row+1:, row:row+1] / pivot) * augmented_mat[row, :]

    x = retroactive_resolution(
        augmented_mat[:, :columns], augmented_mat[:, columns:]
    )

    return x


if __name__ == "__main__":
    import doctest

    doctest.testmod()
