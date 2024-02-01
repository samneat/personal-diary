import pytest
from lib.make_snippet import *

def test_empty_string_returns_empty_string():
    result = make_snippet('')
    assert result == ''

def test_string_less_than_5_returns_string():
    result = make_snippet('one two three four')
    assert result == 'one two three four'

def test_string_of_5_words_returns_string():
    result = make_snippet('one two three four five')
    assert result == 'one two three four five'

def test_more_than_5_words_returns_string_and_elipsis():
    result = make_snippet('one two three four five six')
    assert result == 'one two three four five...'