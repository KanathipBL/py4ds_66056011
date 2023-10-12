"""
Exercise 18 : Buy 8 get 1 free
"""


def get_cost_of_coffee(count, price):
    return (count - count // 9) * price
