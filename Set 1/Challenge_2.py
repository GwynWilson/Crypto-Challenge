from Challenge_1 import *

input_1 = '1c0111001f010100061a024b53535009181c'
input_2 = '686974207468652062756c6c277320657965'

input_1_10 = convertTo10(input_1,16)
input_2_10 = convertTo10(input_2,16)
xor = (input_1_10 ^ input_2_10)
output = convertToHex(xor)

print (output)

if output == '746865206b696420646f6e277420706c6179':
    print ('It Worked')