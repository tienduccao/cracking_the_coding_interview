from q2 import check_permutation


def test_empty_string():
    assert check_permutation('', 'a') == False
    assert check_permutation('', 'ab') == False
    assert check_permutation('', '') == True


def test_the_same_string():
    assert check_permutation('a', 'a') == True
    assert check_permutation('ab', 'ab') == True


def test_permutation_of_two_chars():
    assert check_permutation('ab', 'ba') == True


def test_permutation_of_three_chars():
    assert check_permutation('abc', 'bca') == True
    assert check_permutation('abc', 'bac') == True
    assert check_permutation('abc', 'acb') == True
    assert check_permutation('abc', 'cab') == True
    assert check_permutation('abc', 'cba') == True


def test_non_permutations():
    assert check_permutation('a', 'b') == False
    assert check_permutation('ab', 'cd') == False
    assert check_permutation('ab', 'bc') == False


def test_strings_different_lengths():
    assert check_permutation('a', 'bc') == False
    assert check_permutation('ab', 'abc') == False
    assert check_permutation('ab', 'xyz') == False
