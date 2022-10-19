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

print(xOR_num_and_string("label"))

# 0001101
# ['1100001', '1100010', '1100011']

    
