from Challenge_3 import *
import binascii

input = 'Burning \'em, if you ain\'t quick and nimble I go crazy when I hear a cymbal'
output = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'   
        
key = 'ICE'
print (input)
    
def repeatingKeyXor(string,key):
    out = bytearray()
    index = 0
    for ch in string:       
        to_app = ord(ch) ^ ord(key[index])
        out.append(to_app)
#         print (ch,key[index],chr(to_app))
          
        if index > (len(key) - 2):
            index = 0
        else:
            index += 1
      
    return out
   
if __name__ == "__main__":
    in_xored = repeatingKeyXor(input, key)
    output_unhex = binascii.unhexlify(output)
    print (output_unhex.decode())
    print (in_xored.decode())
    print (in_xored.decode() == output_unhex.decode())


    
        
    