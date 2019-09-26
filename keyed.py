import numpy as np
s=input("Enter the string/plainText	")

s=s.replace(" ","")
s=list(s)
e=[]
print(s)


block_len=int(input("enter the block length"))
if(len(s)%block_len)==0:
    n_block=(len(s)/block_len)
else:
    n_block=int(len(s)/block_len)+1



n_bogus=block_len- (len(s)%block_len)
for i in range(n_bogus):
    s.append('z')

print(s)
print(n_block)
print(block_len)

check=[]
for i in range(0,len(s),5): #step of 5
    check.append([s[i+0],s[i+1],s[i+2],s[i+3],s[i+4]])
print(check) 



print("enter the key for encryption")
key=[]
for j in range(block_len):
    key.append(int(input()))

print(key)

#keyy = dict(input().split() for _ in range(block_len))
#print(keyy)
import copy
copy_check=copy.deepcopy(check)
print(copy_check)

for i in range(n_block):
    for j in range(block_len):
        check[i][j]=copy_check[i][key[j]-1]

print(check)
