s=input("Enter the string(message)")
key=int(input("enter the key value"))

#if any upper case is present
s=s.lower()

print("encryption")
    
c=[]
p=[]
for i in range(0,len(s)):
    c.append(chr(((ord(s[i])-97 +key)%26)+97))
c="".join(c)
print(c)

print("decryption")
for i in range(0,len(s)):
    p.append(chr(((ord(c[i])-97 -key)%26)+97))
p="".join(p)
print(p)
