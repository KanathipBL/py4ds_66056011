"""
Exercise 16
"""


def mode(input):
    """
    Calculate the mode of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int or None: The mode of the list, or None if the list is empty.
    """
    if not input:
        return None
    count = {}
    most_freq, most_freq_count = None, 0
    for number in input:
        count[number] = count.get(number, 0) + 1
        if count[number] > most_freq_count:
            most_freq, most_freq_count = number, count[number]
    return most_freq

