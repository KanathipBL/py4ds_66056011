"""
Exercise 21 : Validate Date
"""


def is_valid_date(year, month, day):
    """
    Check if a given date is valid.

    Parameters:
        year (int): The year of the date.
        month (int): The month of the date.
        day (int): The day of the date.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    # important to import here
    from src.ex20 import is_leap_year

    # fix : complete this
    if not (1 <= month <= 12):
        return False

    if month == 2:
        if is_leap_year(year):
            return 1 <= day <= 29
        else:
            return 1 <= day <= 28

    if month in (1, 3, 5, 7, 8, 10, 12):
        return 1 <= day <= 31

    if month in (4, 6, 9, 11):
        return 1 <= day <= 30

    return True








