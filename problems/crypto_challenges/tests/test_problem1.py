# Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
# Convert from (hex):   49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Convert to (b64):     SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

import pytest
from ..problem1 import convert_hex_to_b64, convert_str_to_hex_bytes

def test_given_example_works():
    given = convert_str_to_hex_bytes("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
    actual = convert_hex_to_b64(given)
    expected = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert actual == expected