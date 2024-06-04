import random
import string


def generate_string(length=5):
    return ''.join(random.choices(string.ascii_letters, k=length))


def generate_int_in_range(min_value, max_value):
    return random.randint(min_value, max_value)
