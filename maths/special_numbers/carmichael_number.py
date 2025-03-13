"""
== Carmichael Numbers ==
A number n is said to be a Carmichael number if it
satisfies the following modular arithmetic condition:

    power(b, n-1) MOD n = 1,
    for all b ranging from 1 to n such that b and
    n are relatively prime, i.e, gcd(b, n) = 1

Examples of Carmichael Numbers: 561, 1105, ...
https://en.wikipedia.org/wiki/Carmichael_number
"""

from functools import lru_cache
from math import gcd as greatest_common_divisor

from maths.greatest_common_divisor import greatest_common_divisor


def power(x: int, y: int, mod: int) -> int:
    """
    Examples:
    >>> power(2, 15, 3)
    2
    >>> power(5, 1, 30)
    5
    """

    result = 1
    x = x % mod
    while y > 0:
        # If y is odd, multiply x with the current result
        if (y & 1) == 1:
            result = (result * x) % mod
        # y must be even now
        y = y >> 1  # Divide y by 2
        x = (x * x) % mod  # Compute x^2
    return result


def is_carmichael_number(n: int) -> bool:
    """
    Examples:
    >>> is_carmichael_number(4)
    False
    >>> is_carmichael_number(561)
    True
    >>> is_carmichael_number(562)
    False
    >>> is_carmichael_number(900)
    False
    >>> is_carmichael_number(1105)
    True
    >>> is_carmichael_number(8911)
    True
    >>> is_carmichael_number(5.1)
    Traceback (most recent call last):
         ...
    ValueError: Number 5.1 must instead be a positive integer

    >>> is_carmichael_number(-7)
    Traceback (most recent call last):
         ...
    ValueError: Number -7 must instead be a positive integer

    >>> is_carmichael_number(0)
    Traceback (most recent call last):
         ...
    ValueError: Number 0 must instead be a positive integer
    """

    if n <= 0 or not isinstance(n, int):
        msg = f"Number {n} must instead be a positive integer"
        raise ValueError(msg)

    for b in range(2, n):
        if memoized_gcd(b, n) == 1 and power(b, n - 1, n) != 1:
            return False
    return True


@lru_cache(None)
def memoized_gcd(a: int, b: int) -> int:
    """
    Calculate Greatest Common Divisor (GCD) with memoization.
    Uses lru_cache to avoid recomputation
    """
    return greatest_common_divisor(a, b)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    number = int(input("Enter number: ").strip())
    if is_carmichael_number(number):
        print(f"{number} is a Carmichael Number.")
    else:
        print(f"{number} is not a Carmichael Number.")
