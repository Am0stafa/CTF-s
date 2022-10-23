def decimalToBinary(n):
    return bin(n).replace("0b", "")
    
def binaryToDecimal(n):
    return int(n,2)      

def xOR(val1,va2):
    collector = ''
    res = []
    for y in range(len(val1)):
        res.append(collector)
        collector = ''
        for x in range(len(val1[y])):
            if val1[y][x] =='1' and va2[x] =='1' or  val1[y][x] == '0' and va2[x] == '0':
                collector +='0'
            elif val1[y][x] == '1' and va2[x] == '0' or val1[y][x] == '0' and va2[x] == '1' :
                collector+='1'
    res.pop(0)
    res.append(collector)
    return res
    
def xOR_num_and_string(a):
    # 0001101
    # ['1100001', '1100010', '1100011']
    listOfAscii =[]
    for x in a:
        listOfAscii.append(ord(x))
    bits = []
    for y in listOfAscii:
        bits.append(decimalToBinary(y))
    num = decimalToBinary(13)
    num = '000'+num
    res = xOR(bits,num)
    listOfDecimal = []
    for i in res:
        listOfDecimal.append(binaryToDecimal(i))
    flag = ''
    for j in listOfDecimal:
        flag+=chr(j)
    
    return flag

# print(xOR_num_and_string("label"))

#& another way to xor number and string

string = "label"
integer = 13
def xOR_num_and_stringV2(string,integer):
    #^ transform to ascii
    unicode_repr = [ord(c) for c in string]
    
    #^ XOR each ascii with the integer
    xor_unicode = [13 ^ i for i in unicode_repr]
    
    #^ return back to string
    xor_string = "".join(chr(o) for o in xor_unicode)
    
    flag = "crypto{" + xor_string + "}"
    print("Flag:")
    print(flag)

def XOR_Properties():
    k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
    k2_k1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
    k2_k3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
    flag_k1_k3_k2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
    
    #^ convert them into numbers to be xor
    k1_ord = [o for o in bytes.fromhex(k1)]
    k2_k3_ord = [o for o in bytes.fromhex(k2_k3)]
    flag_k1_k3_k2_ord = [o for o in bytes.fromhex(flag_k1_k3_k2)]
    
    #! xor
    flag_k1_ord = [o_f132 ^ o23 for (o_f132, o23) in zip(flag_k1_k3_k2_ord, k2_k3_ord)]
    #! xor
    flag_ord = [o_f1 ^ o1 for (o_f1, o1) in zip(flag_k1_ord, k1_ord)]
    
    #^ return back to string
    flag = "".join(chr(o) for o in flag_ord)
    
    print("Flag:")
    print(flag)
    
def findFavNumber():
    #! this function convert hex to ascii then xor each ascii value with number from 0 to 255 as until it starts with crypto
    string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
    
    string_ord = [o for o in bytes.fromhex(string)]
    for order in range(256):
        possible_flag_ord = [order ^ o for o in string_ord]
        possible_flag = "".join(chr(o) for o in possible_flag_ord)
        if possible_flag.startswith("crypto"):
            flag = possible_flag
            break
    
    print("Flag:")
    print(flag)
    
def breakXOREncryption():
    encryptedMsg = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
    encryptedMsg_ord = [o for o in bytes.fromhex(encryptedMsg)]
    flag_format = "crypto{"
    unicode_repr = [ord(c) for c in flag_format]
    keyList = []
    for i in range(len(unicode_repr)):
        keyList.append(unicode_repr[i] ^ encryptedMsg_ord[i])
        
    key = "".join(chr(o) for o in keyList)
    print(key)
    key+='y'
    key_ord = [ord(c) for c in key]
    flag = []
    for i in range(len(encryptedMsg_ord)):
        flag.append(encryptedMsg_ord[i] ^ key_ord[i%len(key)])
        
    flag = "".join(chr(o) for o in flag)
    print("Flag:")
    print(flag)

