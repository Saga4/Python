def alternative_list_arrange(first_input_list: list, second_input_list: list) -> list:
    """
    The method arranges two lists as one list in alternative forms of the list elements.
    :param first_input_list:
    :param second_input_list:
    :return: List
    >>> alternative_list_arrange([1, 2, 3, 4, 5], ["A", "B", "C"])
    [1, 'A', 2, 'B', 3, 'C', 4, 5]
    >>> alternative_list_arrange(["A", "B", "C"], [1, 2, 3, 4, 5])
    ['A', 1, 'B', 2, 'C', 3, 4, 5]
    >>> alternative_list_arrange(["X", "Y", "Z"], [9, 8, 7, 6])
    ['X', 9, 'Y', 8, 'Z', 7, 6]
    >>> alternative_list_arrange([1, 2, 3, 4, 5], [])
    [1, 2, 3, 4, 5]
    """
    output_result_list = []
    
    # Iterate over both lists using zip and extend with remaining elements
    for a, b in zip(first_input_list, second_input_list):
        output_result_list.extend([a, b])
        
    output_result_list.extend(first_input_list[len(second_input_list):])
    output_result_list.extend(second_input_list[len(first_input_list):])

    return output_result_list


if __name__ == "__main__":
    print(alternative_list_arrange(["A", "B", "C"], [1, 2, 3, 4, 5]), end=" ")
