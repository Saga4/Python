"""
This is a pure Python implementation of the merge-insertion sort algorithm
Source: https://en.wikipedia.org/wiki/Merge-insertion_sort

For doctests run following command:
python3 -m doctest -v merge_insertion_sort.py
or
python -m doctest -v merge_insertion_sort.py

For manual testing run:
python3 merge_insertion_sort.py
"""

from __future__ import annotations

from bisect import insort_left


def binary_search_insertion(sorted_list, item):
    """
    Insert an item into a sorted list using binary search to find the position.
    
    >>> binary_search_insertion([1, 2, 7, 9, 10], 4)
    [1, 2, 4, 7, 9, 10]
    """
    insort_left(sorted_list, item)
    return sorted_list


def merge(left, right):
    """
    >>> merge([[1, 6], [9, 10]], [[2, 3], [4, 5], [7, 8]])
    [[1, 6], [2, 3], [4, 5], [7, 8], [9, 10]]
    """
    result = []
    while left and right:
        if left[0][0] < right[0][0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right


def sortlist_2d(list_2d):
    """
    Recursively sort a list of lists based on the first element of each list.
    
    >>> sortlist_2d([[9, 10], [1, 6], [7, 8], [2, 3], [4, 5]])
    [[1, 6], [2, 3], [4, 5], [7, 8], [9, 10]]
    """
    length = len(list_2d)
    if length <= 1:
        return list_2d
    middle = length // 2
    return merge(sortlist_2d(list_2d[:middle]), sortlist_2d(list_2d[middle:]))


def merge_insertion_sort(collection: list[int]) -> list[int]:
    """
    Pure implementation of merge-insertion sort algorithm in Python.
    
    :param collection: some mutable ordered collection with heterogeneous comparable items inside
    :return: the same collection ordered by ascending
    
    Examples:
    >>> merge_insertion_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> merge_insertion_sort([99])
    [99]
    >>> merge_insertion_sort([-2, -5, -45])
    [-45, -5, -2]
    >>> import itertools
    >>> permutations = list(itertools.permutations([0, 1, 2, 3, 4]))
    >>> all(merge_insertion_sort(list(p)) == [0, 1, 2, 3, 4] for p in permutations)
    True
    """

    if len(collection) <= 1:
        return collection
    
    # Group the items into two pairs
    paired_list = [[min(collection[i], collection[i + 1]), max(collection[i], collection[i + 1])]
                   for i in range(0, len(collection) - 1, 2)]
    last_odd_item = collection[-1] if len(collection) % 2 else None
    
    # Sort the paired list
    sorted_paired_list = sortlist_2d(paired_list)
    
    result = [item[0] for item in sorted_paired_list]
    result.append(sorted_paired_list[-1][1])
    
    # Insert the last odd item if it exists
    if last_odd_item is not None:
        binary_search_insertion(result, last_odd_item)
    
    # Insert remaining items
    for item in sorted_paired_list[:-1]:
        binary_search_insertion(result, item[1])
    
    return result


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(merge_insertion_sort(unsorted))
