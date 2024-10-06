### The Question:

Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?

The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.

To illustrate:

    ```
      message: HELLO
      ascii bytes: [72, 69, 76, 76, 79]
      hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
      base-16: 0x48454c4c4f
      base-10: 310400273487
    ```

Convert the following integer back into a message:

11515195063862318899931685488813747395775516287289682636499965282714637259206269
---

### Explanation:

To convert a large integer back into a message, we need to reverse the process described in the question. Here's a step-by-step explanation of the approach:

1. Convert the integer to hexadecimal:
   The first step is to convert the given large integer (base-10) to its hexadecimal (base-16) representation. This is done because hexadecimal is a more convenient representation for working with bytes.

2. Split the hexadecimal string into bytes:
   Once we have the hexadecimal string, we need to split it into byte-sized chunks. In hexadecimal, each byte is represented by two characters.

3. Convert hexadecimal bytes to ASCII characters:
   For each byte (represented as a two-character hexadecimal string), we convert it to its corresponding ASCII character.

4. Combine the ASCII characters:
   Finally, we join all the ASCII characters to form the original message.

This approach is efficient and works well for cryptographic purposes because:
- It's reversible: We can convert messages to numbers and back without loss of information.
- It's compact: It represents the message as a single large number, which is suitable for mathematical operations in cryptosystems like RSA.
- It preserves the order of characters: The concatenation of hexadecimal bytes maintains the original sequence of characters in the message.

---

### Solution:

Here's a Python implementation to solve the challenge:

```python
def int_to_hex(n):
    return hex(n)[2:]  # Remove '0x' prefix

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
```
---
