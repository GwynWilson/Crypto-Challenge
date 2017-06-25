hex = '0123456789abcdef'
_64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def convertToBinary(num):
    list = []
    while num > 0:
        rem = num%2
        num = num//2
        
        list.append(rem)

    output = ''
    for num in list[::-1]:
        output += str(num)

    else:
        return output

def convertTo10(num,base):
    output = 0
    power = len(num) - 1
    for v in num:
        output += (hex.index(v)*(base**(power)))
        power -= 1
    return output
    

def convertToHex(num):
    list = []
    while num > 0:
        rem = num%16
        num = num//16
        
        list.append(hex[rem])

    output = ''
    for num in list[::-1]:
        output += str(num)
    
    return output

def convertTo64(num):
    list = []
    while num > 0:
        rem = num%64
        num = num//64
        list.append(_64[rem])
    output = ''
    for num in list[::-1]:
        output += str(num)
    return output

def convertHexTo64(hex):
    base_10 = convertTo10(hex,16)
    return convertTo64(base_10)

# input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
# output = (convertHexTo64(input))
# if output == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t':
#     print ('It Worked')

