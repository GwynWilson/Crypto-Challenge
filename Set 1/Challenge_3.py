from Challenge_1 import *
import binascii
input = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

letter_freq = {'e':12,'t':9,'a':8,'o':7,'i':7,'n':7,'s':6,'h':6,'r':6,'d':4,'l':4,'c':3,'u':3,
               'm':2,'w':1,'f':2,'g':2,'y':2,'p':2,'b':1,'v':1,'k':1,'j':1,'x':1,'q':1,'z':1}

input_data = binascii.unhexlify(input)

def decryptWithKey(input_data,let):
    key = ord(let)    
    decrypt = [chr(byte^key) for byte in input_data]
    out = ''
    for ch in decrypt:
        out += ch
    return out

def score(str):
    scr = 0
    str_l = str.lower()
    for let in str:
        if let in letter_freq.keys():
            scr += letter_freq[let]
    return scr

allChr = {}
for ch in alphabet:
    string = decryptWithKey(input_data,ch)
    scr = score(string)
    allChr[string] = (scr,ch)
    
def bestResults(dic,n=5):
    top = []
    v = list(dic.values())
    v_v = [x[0] for x in v]
    k = list(dic.keys())

    while len(top)<6:
        v_v_max = max(v_v)
        v_v_index = v_v.index(v_v_max)
        cor_v = v[v_v_index]
        key = k[v_v_index]
        top.append((key,cor_v))
        
        k.remove(key)
        v_v.remove(v_v_max)
        v.remove(cor_v)
    return top

top_5 = bestResults(allChr)
print ("Top 5 answers are:")
print (top_5)

answer = top_5[1]
print ("Final answer and characters:")
print (answer[0],":",answer[1][1])


    