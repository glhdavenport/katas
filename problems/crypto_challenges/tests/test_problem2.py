# Fixed XOR
# Write a function that takes two equal-length buffers and produces their XOR combination.

# If your function works properly, then when you feed it the string:

# 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against:

# 686974207468652062756c6c277320657965
# ... should produce:

# 746865206b696420646f6e277420706c6179

from ..problem1 import convert_str_to_hex_bytes
from ..problem2 import hex_XOR

def test_given_example_works_XOR():
    given_1 = convert_str_to_hex_bytes("1c0111001f010100061a024b53535009181c")
    given_2 = convert_str_to_hex_bytes("686974207468652062756c6c277320657965")
    actual = hex_XOR(given_1, given_2)
    expected = convert_str_to_hex_bytes("746865206b696420646f6e277420706c6179")
    assert actual == expected
    
