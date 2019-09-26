s=input("Enter the string(message)")
k1,k2=(input("enter the key value")).split()
k1=int(k1)
k2=int(k2)


#if any upper case is present
s=s.lower()

print("encryption")
    
c=[]
p=[]
for i in range(0,len(s)):
    c.append(chr((((ord(s[i])-97) *k1+k2)%26)+97))
c="".join(c)
print("encryption msg is")
print(c)


print(".........................................")
def findkeyInverse(r1,r2):
    t1=0
    t2=1
    while(r2>0):
        q=int(r1/r2)
        r=r1-(q*r2)
        r1=r2
        r2=r
        t=t1-(q*t2)
        t1=t2
        t2=t
        #print(r1)
        #print("and")
        #print(r2)
        #print(".....")
        
        
    if r1==1:
        b_inv=t1
    else:
        b_inv=1
    k_inv= b_inv % 26
    return k_inv


print("decryption")

z= findkeyInverse(26,k1)
print("key inverse is",z)

print(".........................................")

for i in range(0,len(s)):
    p.append(chr(((((ord(c[i])-97) -k2)*z)%26)+97))
p="".join(p)
print("decrypted msg is")
print(p)
