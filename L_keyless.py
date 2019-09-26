import numpy as np
s=input("Enter the string/plainText	")
e=[]
print(s)
check=[]
for i in range(len(s)):
	if s[i]==" ":
		check.append(i)
s= s.replace(" ","")


d = np.zeros((2,len(s)),dtype=str)

print(d)

j=0
for i in range(len(s)):
	d[j][i]=s[i]
	if j==0:
		j=1	
	else:
		j=0

print(d)


msg=""
for i in range(len(s)):
	msg+=d[j][i]
		
	if j==0:
		j=1	
	else:
		j=0

print("Encrypted meggase is")
msg= list(msg)
for i in check:
	msg.insert(i," ")
msg = ''.join(msg)
print(msg)





