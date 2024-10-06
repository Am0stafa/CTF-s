### The Question:

Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using an alphabet of 64 characters. One character of a Base64 string encodes 6 binary digits (bits), and so 4 characters of Base64 encode three 8-bit bytes.

Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.

Take the below hex string, decode it into bytes and then encode it into Base64.

72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf

---

### Explanation:

Base64 encoding is a method of representing binary data using a set of 64 characters. It's commonly used to encode binary data that needs to be stored and transferred over media that are designed to deal with text. This encoding helps to ensure that the data remains intact without modification during transport.

In this challenge, we're dealing with two encoding schemes:

1. Hexadecimal (hex): A base-16 system that uses 16 distinct symbols (0-9 and A-F) to represent binary data. Each hex digit represents 4 bits, so 2 hex digits represent 1 byte (8 bits).

2. Base64: A base-64 system that uses 64 distinct symbols (A-Z, a-z, 0-9, +, /) to represent binary data. Each Base64 digit represents 6 bits, so 4 Base64 characters represent 3 bytes (24 bits).

The process to solve this challenge involves two main steps:

1. Decoding the hex string into bytes:
   - Each pair of hex characters represents one byte.
   - We use Python's `binascii.unhexlify()` function to convert the hex string to bytes efficiently.

2. Encoding the bytes into Base64:
   - We use Python's `base64.b64encode()` function to convert the bytes to Base64.
   - The result is a bytes object, which we decode to a UTF-8 string for readability.

This approach is efficient and leverages Python's built-in libraries, making the code concise and easy to understand.

---

### Solution:

Here's the Python code to solve this challenge:

```python
import binascii
import base64

# Define the input hex string
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Convert hex to bytes
byte_data = binascii.unhexlify(hex_string)

# Encode bytes to Base64
base64_encoded = base64.b64encode(byte_data).decode('utf-8')

print(f"Base64 encoded result: {base64_encoded}")
```

---