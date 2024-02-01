from lib.count_words import *

def test_return_zero_for_empty_string():
    result = count_words('')
    assert result == 0

def test_return_5_for_string_of_5_words():
    result = count_words('one two three four five')
    assert result == 5