import binascii
import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# 1. Convert hex to bytes
byte_data = binascii.unhexlify(hex_string)

# 2. Encode bytes to Base64
base64_encoded = base64.b64encode(byte_data).decode('utf-8')

print(f"Base64 encoded result: {base64_encoded}")
