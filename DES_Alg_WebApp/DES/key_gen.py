import numpy as np 
import math
from random import randrange, getrandbits

hexcodes = {
    '0000':'0',
    '0001':'1',
    '0010':'2',
    '0011':'3',
    '0100':'4',
    '0101':'5',
    '0110':'6',
    '0111':'7',
    '1000':'8',
    '1001':'9',
    '1010':'A',
    '1011':'B',
    '1100':'C',
    '1101':'D',
    '1110':'E',
    '1111':'F',
}

hex2bincodes = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',
}

def bin2hex(input_):
    output = ''
    for i in range(0,len(input_),4):
        s = input_[i:i+4]
        # print(int(s,2))
        output+=hexcodes[s]
    return output

def hex2bin(input_):
    output = ''
    for i in range(0,len(input_)):
        output+=hex2bincodes[input_[i]]
    return output


def format_bin(input,dist):
    output = ''
    for i in range(0,len(input),dist):
        s = input[i:i+dist]
        # print(int(s,2))
        output+=s
        output+=' '
    output = output.strip()
    return output


def bin2string(input):
    output = ''
    for i in range(0,len(input),8):
        s = input[i:i+8]
        a = int(s,2)
        output+=chr(a)
    output = output.strip()
    return output


def string2Bin(input_):
    output = ''
    for i in input_:
        a = ord(i)
        output+='{0:08b}'.format(a)
    output = output.strip()
    return output


def is_prime(n, k=128):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True
def generate_prime_candidate(length):
    p = getrandbits(length)
    p |= (1 << length - 1) | 1
    return p
def generate_prime_number(length=1024):
    p = 4
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p

bit_table = [ 57,49,41,33,25,17,9, 
        1,58,50,42,34,26,18, 
        10,2,59,51,43,35,27, 
        19,11,3,60,52,44,36,           
        63,55,47,39,31,23,15, 
        7,62,54,46,38,30,22, 
        14,6,61,53,45,37,29, 
        21,13,5,28,20,12,4]


def ParityDrop(ini_key, bit_table):
    key = []
    for i in range(0,56):
        key.append(ini_key[bit_table[i]-1])
    key = np.array(key)
    return key



def ShiftLeft(Lkey, Rkey, ind):
    if ind in [1,2,9,16]:
        bit_shift=-1
    else:
        bit_shift=-2
    out_left = np.roll(Lkey,bit_shift)
    out_right = np.roll(Rkey,bit_shift)
    return out_left, out_right

compression_hash =  [14,17,11,24,1,5,3,28,15,6,21,10,23,
                    19,12,4,26,8,16,7,27,20,13,2,41,52,31,
                    37,47,55,30,40,51,45,33,48,44,49,39,56,
                    34,53,46,42,50,36,29,32]

def compression_PBox(L,R):
    temp = np.concatenate((L,R),axis=0)
    compressed = np.zeros((48,))
    for i in range(48):
        ind = compression_hash[i];
        compressed[i] =  temp[ind-1]
    compressed = compressed.astype(int)
    return compressed


def key_generator(Key = None):
    # if Key is None:
    #     Key = generate_prime_number(length=64)
    ini_key = Key
    key_final = ParityDrop(ini_key, bit_table)
    L = key_final[:28]
    R = key_final[28:]
    keys = []
    for i in range(1,17):
        L, R = ShiftLeft(L, R, i)
        key = compression_PBox(L, R)
        keys.append(key)
    return keys





