from utils import string_to_counter


def is_panlindrome_permutation(string):
    char_counter = string_to_counter(string.lower())

    odd_char_count = 0
    for _, char_count in char_counter.items():
        if char_count % 2 == 1:
            odd_char_count += 1

    return odd_char_count <= 1
