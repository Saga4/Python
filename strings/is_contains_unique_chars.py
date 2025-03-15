def is_contains_unique_chars(input_str: str) -> bool:
    """
    Check if all characters in the string are unique or not.
    >>> is_contains_unique_chars("I_love.py")
    True
    >>> is_contains_unique_chars("I don't love Python")
    False

    Time complexity: O(n)
    Space complexity: O(min(n, 144697)) as there are 144697 characters in unicode.
    """

    seen_chars = set()
    for ch in input_str:
        if ch in seen_chars:
            return False
        seen_chars.add(ch)
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
