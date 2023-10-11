"""
Exercise 15
"""


def median(input):
    """
    Calculate the median of a list of numbers.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        [int, None]: The median value of the list, or None if the list is empty.
    """
    if not input:
        return None
    sorted_input = sorted(input)
    middle = len(sorted_input) // 2
    return (sorted_input[middle - 1] + sorted_input[middle]) / 2 if len(sorted_input) % 2 == 0 else sorted_input[middle]

