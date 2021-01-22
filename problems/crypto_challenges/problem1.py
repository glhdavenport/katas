# Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
# Convert from (hex):   49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Convert to (b64):     SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

from binascii import a2b_hex
import binhex
from base64 import b64encode

def convert_hex_to_b64(hex_bytes):
    return b64encode(hex_bytes)

def convert_str_to_hex_bytes(string):
    return a2b_hex(string)