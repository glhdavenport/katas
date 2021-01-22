# This works if XORing a string against a single character
def hex_XOR_String(long_byte_string1, byte_char):
    first, second = bytearray(long_byte_string1), bytearray(byte_char)
    result = bytearray(len(first))
    for index, value in enumerate(first):
        print(f"Value: {len(bytearray(str(value), 'utf-8'))}, Second: {len(second)}, Everything: {len(hex_XOR(value, second))}")
        result[index] = hex_XOR(value, second)
    return result

# This works if strings are the same length
def hex_XOR(byte_string1, byte_string2):
    first, second = bytearray(byte_string1), bytearray(byte_string2)
    result = bytearray(len(first))
    shortest = min(len(first), len(second))
    for i in range(shortest):
        result[i] = first[i] ^ second[i]
        print(type(first[i] ^ second[i]))
    return result