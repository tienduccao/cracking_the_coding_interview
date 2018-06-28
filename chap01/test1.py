from q1 import has_all_unique_characters, has_all_unique_characters2


def base_test(string, value=True):
    assert has_all_unique_characters(string) == value
    assert has_all_unique_characters2(string) == value


def test_zero_char():
    base_test('')


def test_one_char():
    base_test('a')


def test_two_chars():
    base_test('ab')


def test_duplicated_chars():
    base_test('aa', False)
    base_test('aaa', False)


def test_some_duplicated_chars():
    base_test('aba', False)
    base_test('abb', False)


def test_lower_upper_chars():
    base_test('aA')


def test_non_alphabet_char():
    base_test('*')
