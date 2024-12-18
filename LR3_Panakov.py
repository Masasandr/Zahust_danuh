import sys
import math

def xor(a, b):
    res = ''
    for i in range(len(a)):
        res += hex(int(a[i], 16) ^ int(b[i], 16))[2:] 
    return res

input1 = input()
input2 = input()
input3 = input()

result = xor(xor(input1, input2), input3)

decoded_message = ''.join(chr(int(result[i:i+2], 16)) for i in range(0, len(result), 2))

print(decoded_message)