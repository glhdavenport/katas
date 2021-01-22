import pytest
from ..prefix import is_prefix, is_prefix_of_word, words

def test_three_word_sentence_is_three_words_long():
    """Given a sentence with three words
    when we count the number of words
    then we get 3 back"""
    
    given = "three words here"
    expected = 3
    actual = len(words(given))
    assert expected == actual

def test_sentence_has_more_than_one_word():
    given = "More than one word"
    actual = words(given)
    assert len(actual) > 1

def test_empty_sentence_has_no_words():
    given = ""
    actual = len(words(given))
    expected = 0
    assert actual == expected

def test_prefix_in_word():
    given_word = "hamburger"
    given_prefix = "ham"
    actual = is_prefix(given_word, given_prefix)
    expected = True
    assert actual == expected

def test_if_prefix_matches_then_return_index():
    given_sentence = "i love eating burger"
    given_prefix = "burg"
    actual = is_prefix_of_word(given_sentence, given_prefix)
    expected = 4
    assert actual == expected

def test_if_prefix_is_not_in_sentence_return_neg_one():
    given_sentence = "happy times"
    given_prefix = "sad"
    actual = is_prefix_of_word(given_sentence, given_prefix)
    expected = -1
    assert actual == expected