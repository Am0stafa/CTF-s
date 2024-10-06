
KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY2_XOR_KEY1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
KEY2_XOR_KEY3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

# flag XOR n = key1 XOR key3 XOR key2
# flag = key1 XOR key3 XOR key2 XOR n

# XOR operation for bytes objects
def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

key2 = xor_bytes(KEY1, KEY2_XOR_KEY1)
key3 = xor_bytes(key2, KEY2_XOR_KEY3)
flag_bytes = xor_bytes(xor_bytes(xor_bytes(KEY1, key3), key2), FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2)
# convert flag_bytes to hex
flag_hex = flag_bytes.hex()
# convert flag_hex to decimal
flag_decimal = int(flag_hex, 16)
# convert flag_decimal to bytes
flag = bytes.fromhex(hex(flag_decimal)[2:]).decode('utf-8')

print(flag)

