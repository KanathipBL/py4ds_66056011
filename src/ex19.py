"""
Exercise 19 : Password Generator
"""
import random

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'    # 26
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # 26
NUMBERS = '1234567890'                          # 10
SPECIAL = '~!@#$%^&*()_+'                       # 13

ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL


def gen_password(length):

    # fix : complete this
    length = max(length, 12)
    password = [
        random.choice(LOWER_LETTERS),
        random.choice(UPPER_LETTERS),
        random.choice(NUMBERS),
        random.choice(SPECIAL)
    ]

    while len(password) < length:
        password.append(random.choice(ALL_CHARS))

    random.shuffle(password)
    return ''.join(password)

