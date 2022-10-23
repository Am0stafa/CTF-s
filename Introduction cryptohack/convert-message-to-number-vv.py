'Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?'
'For how they work under the hood, ref ss 1'

from Crypto.Util.number import *

number = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
word = 'crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}'


def convertToMessage(message):
    return long_to_bytes(message).decode("utf-8") 
    #finally convert from bytes to string
    
def convertToNumber(word):
    return bytes_to_long(bytes(word, 'utf-8'))
    #finally convert from string to bytes

