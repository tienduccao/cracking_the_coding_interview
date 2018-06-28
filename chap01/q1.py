from collections import Counter


def has_all_unique_characters(string):
    char_counter = Counter()
    for char in string:
        char_counter[char] += 1
    return len(char_counter.keys()) == len(string)


# This version doesn't use HashMap (Dictionary) data structure
def has_all_unique_characters2(string):
    for i, ch_i in enumerate(string):
        for _, ch_j in enumerate(string[i + 1:]):
            if ch_i == ch_j:
                return False
    return True
