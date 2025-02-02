"""
Execise 12
"""


def get_smallest(numlist):
    """
    Get the smallest number from a list of numbers.

    Args:
        num_list (list): A list of numbers.

    Returns:
        int or None: The smallest number from the list. If the list is empty, returns None.
    """
    return min(numlist, default=None)
