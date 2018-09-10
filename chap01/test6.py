from q6 import compress_string


def test_one_character():
    assert compress_string('aaa') == 'a3'


def test_two_characters():
    assert compress_string('aaabb') == 'a3b2'


def test_single_left_most_character():
    assert compress_string('abbbb') == 'a1b4'
    assert compress_string('abccccc') == 'a1b1c5'


def test_single_right_most_character():
    assert compress_string('aaaab') == 'a4b1'
    assert compress_string('aaaabc') == 'aaaabc'
    assert compress_string('aaaabbc') == 'a4b2c1'


def test_compressed_not_smaller_than_original():
    assert compress_string('a') == 'a'
    assert compress_string('aa') == 'aa'
    assert compress_string('ab') == 'ab'
    assert compress_string('aabb') == 'aabb'
    assert compress_string('aaab') == 'aaab'
    assert compress_string('abc') == 'abc'


def test_book_example():
    assert compress_string('aabcccccaaa') == 'a2b1c5a3'


def test_upper_and_lower_case():
    assert compress_string('AAbbb') == 'A2b3'
    assert compress_string('AAaaa') == 'A2a3'
