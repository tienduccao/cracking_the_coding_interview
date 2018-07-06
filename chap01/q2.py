from utils import string_to_counter


def check_permutation(s1, s2):
    c1, c2 = string_to_counter(s1), string_to_counter(s2)
    if len(c1) == len(c2):
        for char, count1 in c1.items():
            if char not in c2:
                return False
            if count1 != c2[char]:
                return False
        return True
    return False
