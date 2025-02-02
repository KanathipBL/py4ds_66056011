"""
Exercise 14
"""


def average(input) -> float:
    """
    Calculate the average of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - float: The average of the numbers in the list.
      If the list is empty, returns 0.
    """
    if len(input) == 0:
        return None
    total = 0

    for number in input:
        total += number
    return total / len(input)

#%%
