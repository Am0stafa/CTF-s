def int_to_hex(n):
    """
    Convert a decimal (base-10) integer to hexadecimal (base-16) string.

    This function takes an integer in base-10 and converts it to its
    hexadecimal representation. The resulting string does not include
    the '0x' prefix typically used to denote hexadecimal numbers.

    Args:
        n (int): The decimal integer to convert.

    Returns:
        str: The hexadecimal representation of the input integer,
             without the '0x' prefix.
    """
    return hex(n)[2:]

def split_hex_to_bytes(hex_string):
    return [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]

def hex_bytes_to_ascii(hex_bytes):
    return ''.join(chr(int(byte, 16)) for byte in hex_bytes)

def decrypt_message(encrypted_int):
    hex_string = int_to_hex(encrypted_int)
    hex_bytes = split_hex_to_bytes(hex_string)
    return hex_bytes_to_ascii(hex_bytes)

# The encrypted integer
encrypted = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Decrypt the message
decrypted_message = decrypt_message(encrypted)
print(f"Decrypted message: {decrypted_message}")
