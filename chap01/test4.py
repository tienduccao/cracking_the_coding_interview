from q4 import is_panlindrome_permutation


def test_string_of_one_char():
    assert is_panlindrome_permutation('a') == True


def test_string_of_two_chars():
    assert is_panlindrome_permutation('ab') == False
    assert is_panlindrome_permutation('aa') == True


def test_string_of_three_chars():
    assert is_panlindrome_permutation('aba') == True
    assert is_panlindrome_permutation('a a') == True
    assert is_panlindrome_permutation('a*a') == True
    assert is_panlindrome_permutation('a c') == False


def test_string_of_four_chars():
    assert is_panlindrome_permutation('abab') == True
    assert is_panlindrome_permutation('a a ') == True
    assert is_panlindrome_permutation('a*a*') == True
    assert is_panlindrome_permutation('a ca') == False


def test_sample_example():
    '''
    Example from the book but the space character must be removed
    '''
    assert is_panlindrome_permutation('TactCoa') == True
