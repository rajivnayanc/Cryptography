import numpy as np 
from .key_gen import *

expansion_hash = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,
     			  12,13,14,15,16,17,16,17,18,19,20,21,20,21,
     			  22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]

# print(len(expansion_hash))
def expansion_PBox(R):
	expanded = np.zeros((48,))
	R = list(map(int,R))
	for i in range(48):
		ind = expansion_hash[i];
		expanded[i] =  R[ind-1]
	expanded = expanded.astype(int)
	expanded = expanded.tolist()
	expanded = list(map(str,expanded))
	expanded = ''.join(expanded)
	return expanded

straight_hash = [16, 7, 20, 21, 29, 12, 28, 17,
     			 1, 15, 23, 26, 5, 18, 31, 10,
     			 2, 8, 24, 14, 32, 27, 3, 9,
     			 19, 13, 30, 6, 22, 11, 4, 25]


# print(len(straight_hash))
def straight_PBox(expanded):
	R = np.zeros((32,))
	expanded = list(map(int,expanded))
	for i in range(32):
		ind = straight_hash[i];
		R[i] =  expanded[ind-1]
	R = R.astype(int)
	R = R.tolist()
	R = list(map(str,R))
	R = ''.join(R)
	return R

S = {}

S[0] = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7, 
        0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8, 
        4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0, 
        15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]

S[1] = [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10, 
        3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5, 
        0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15, 
        13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]

S[2] = [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8, 
        13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1, 
        13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7, 
        1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]

S[3] = [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15, 
        13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9, 
        10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4, 
        3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]

S[4] = [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9, 
        14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6, 
        4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14, 
        11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]

S[5] =  [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11, 
        10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8, 
        9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6, 
        4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]

S[6] = [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1, 
        13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6, 
        1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2, 
        6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]

S[7] = [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7, 
        1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2, 
        7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8, 
        2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11] 

def S_boxes(input_):
	output = ''
	k = 0
	for i in range(0,len(input_),6):
		substr = input_[i:i+6]
		r =''
		r+=substr[0]
		r+=substr[5]
		c = substr[1:5]
		# print("~~{}".format(k+1),substr,r,c,end='')
		r = int(r,2)
		c = int(c,2)
		value = S[k][r*16+c]
		# print("~~",r,c,value)
		output += '{0:04b}'.format(value)
		k+=1
	output = output.strip()
	return output
# print(S_boxes('100011010101000000'))

def xor_(a,b):
	output = ''
	for i in range(len(a)):
		if a[i]==b[i]:
			output+='0'
		else:
			output+='1'
	return output

def DEF_FUNCTION(R,Ki):
	R = expansion_PBox(R)
	R = xor_(R,Ki)
	R = S_boxes(R)
	R = straight_PBox(R)
	return R

initial_PHash = [58,50,42,34,26,18,10,2, 
		        60,52,44,36,28,20,12,4, 
		        62,54,46,38,30,22,14,6, 
		        64,56,48,40,32,24,16,8, 
		        57,49,41,33,25,17,9,1, 
		        59,51,43,35,27,19,11,3, 
		        61,53,45,37,29,21,13,5, 
		        63,55,47,39,31,23,15,7]

def initial_Perm(input_):
	R = np.zeros((64,))
	input_ = list(map(int,input_))
	for i in range(64):
		ind = initial_PHash[i];
		R[i] =  input_[ind-1]
	R = R.astype(int)
	R = R.tolist()
	R = list(map(str,R))
	R = ''.join(R)
	return R


final_FHash = [40,8,48,16,56,24,64,32, 
		        39,7,47,15,55,23,63,31, 
		        38,6,46,14,54,22,62,30, 
		        37,5,45,13,53,21,61,29, 
		        36,4,44,12,52,20,60,28, 
		        35,3,43,11,51,19,59,27, 
		        34,2,42,10,50,18,58,26, 
		        33,1,41,9,49,17,57,25]
		       
def final_Perm(input_):
	R = np.zeros((64,))
	input_ = list(map(int,input_))
	for i in range(64):
		ind = final_FHash[i];
		R[i] =  input_[ind-1]
	R = R.astype(int)
	R = R.tolist()
	R = list(map(str,R))
	R = ''.join(R)
	return R

def fiestal_Block(input_,key):
	L = input_[:32]
	R = input_[32:]
	key = list(map(str,key))
	key = ''.join(key)
	R_ = DEF_FUNCTION(R,key)
	L_ = xor_(L,R_)
	output = R+L_ 
	return output

def encrypt(message,keys):
	m_Bin = string2Bin(message)
	output = initial_Perm(m_Bin)
	for i in range(16):
		output = fiestal_Block(output,keys[i])
	L = output[:32]
	R = output[32:]
	output = R+L
	output = final_Perm(output)
	# output = bin2hex(output)
	return output

def decrypt(Cipher,keys):
	output = Cipher
	decipher = initial_Perm(output)
	for i in range(16):
		decipher = fiestal_Block(decipher,keys[15-i])
	L = decipher[:32]
	R = decipher[32:]
	decipher = R+L
	decipher = final_Perm(decipher)
	# decipher = bin2string(decipher)
	return decipher



def encryption(message,Key):
	keys = key_generator(Key)
	rem = math.ceil(len(message)/8)*8 -len(message)
	mess_new =''
	mess_new+=message
	for i in range(rem):
		mess_new+='~'
	# print(mess_new)
	cipher = ''
	for i in range(0,len(mess_new),8):
		msg = mess_new[i:i+8]
		cipher+=encrypt(msg,keys)
	return cipher

def decryption(message,Key):
	keys = key_generator(Key)
	rem = math.ceil(len(message)/64)*64 -len(message)
	mess_new =message
	cipher=''
	for i in range(0,len(mess_new),64):
		msg = mess_new[i:i+64]
		d = decrypt(msg,keys)
		# print(len(d))
		cipher+=d
	return cipher

def process(input_):
	output = ''
	for ch in input_:
		if ch!='~':
			output+=ch
	return output



