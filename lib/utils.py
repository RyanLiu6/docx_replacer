from random import randint


class replace_types:
    every = "all"
    tables = "tables"
    headings = "headings"
    paragraphs = "paragraphs"


REPLACE_TYPES = [
    replace_types.every,
    replace_types.tables,
    replace_types.headings,
    replace_types.paragraphs
]


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
