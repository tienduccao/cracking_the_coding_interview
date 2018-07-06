from collections import Counter


def string_to_counter(s):
    c = Counter()
    for char in s:
        c[char] += 1
    return c
