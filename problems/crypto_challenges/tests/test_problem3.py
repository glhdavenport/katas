# Single-byte XOR cipher
# The hex encoded string:

# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.

# You can do this by hand. But don't: write code to do it for you.

# How? Devise some method for "scoring" a piece of English plaintext.
# Character frequency is a good metric. Evaluate each output and choose the one with the best score.
import string
import pytest
from ..problem1 import convert_str_to_hex_bytes
from ..problem2 import hex_XOR, hex_XOR_String
from ..problem3 import get_sentence_score

@pytest.mark.skip(reason="Not sure that the input is actually correct")
def test_get_sentence_score():
    # sentence = b"The quick brown fox jumps over the lazy dog."
    sentence = convert_str_to_hex_bytes("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    actual = get_sentence_score(sentence)
    expected = 31158
    assert actual == expected 

@pytest.mark.skip(reason="Not sure that the inputs are actually correct")
def test_unscrambled_pangram_scores_better_than_scrambled_pangram():
    unscrambled_pangram = b"The quick brown fox jumps over the lazy dog."
    scrambled_pangram = b"Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph."
    unscrambled_actual = get_sentence_score(unscrambled_pangram)
    scrambled_actual = get_sentence_score(scrambled_pangram)
    assert scrambled_actual < unscrambled_actual

# rework this to be in hex 
def test_the_thing_with_a_righteous_name():
    given_1 = convert_str_to_hex_bytes("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    results = {}
    for letter in string.ascii_letters:
        current_letter = bytearray(letter, 'utf-8')
        xor_sentence = hex_XOR_String(given_1, current_letter)
        current_score = get_sentence_score(xor_sentence)
        results[letter] = current_score
    print("Results: ", results)
    assert results == None