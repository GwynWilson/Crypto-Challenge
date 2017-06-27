from Challenge_1 import *
import binascii
input = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# getText = "686974207468652062756c6c277320657965"
# getText_data = binascii.unhexlify(getText)
# print (binascii.b2a_qp(getText_data))

input_data = binascii.unhexlify(input)

key = ord('a')
print (key)
       
decrypt = [chr(byte^key) for byte in input_data]
out = ''
for ch in decrypt:
    out += ch
print (out)