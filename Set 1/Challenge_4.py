from Challenge_3 import *
import binascii

all_strings = []
with open("Data_4.txt","r") as f:
    for line in f:
        all_strings.append(line.strip())

def all_xor(input):
    #Function collecting the processes from Challenge_3
    input_data = binascii.unhexlify(input)
    
    allChr = {}
    for ch in alphabet:
        string = decryptWithKey(input_data,ch)
        scr = score(string)
        allChr[string] = (scr,ch)
        
    return bestResults(allChr,1)
    

for string in all_strings:
    best = all_xor(string)
    if best[1][0] > 100:
            print (best)
