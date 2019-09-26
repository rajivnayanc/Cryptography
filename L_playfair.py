key = [ [ "L", "G", "D", "B", "A" ],
       	[ "Q", "M", "H", "E", "C" ],
       	[ "U", "R", "N", "I", "F" ],
       	[ "X", "V", "S", "O", "K" ],
       	[ "Z", "Y", "W", "T", "P" ]
	  ]

s=list(input("Enter the string/plainText	"))
e=[]
print(s)
print("the bogus letter is X")
check=[]

for i in range(len(s)):
	if s[i]==s[i-1]:
		check.append(i)

for i in range(len(s)):
	if s[i]=="J":
		s[i]="I"

for c in check:
	s.insert(c,"X")

for i in range(len(s)):
	if s[i]=="J":
		s[i]="J"

print(s)			

if len(s)%2!=0:
	s.append("X")

flag=0

for i in range(0,len(s)-1,2):
	k=i+1
	for j in range(0,5):
		if s[i] in key[j]:
			indexiI=j
			indexiJ=key[j].index(s[i])

			if s[k] in key[j]:
				indexkI=j
				indexkJ=key[j].index(s[k])
			
				e.append(key[j][indexiJ+1])
				e.append(key[j][indexkJ+1])
				flag=1

			else:
				for b in range(5):
					if s[k] == key[b][indexiJ]:
							e.append(key[j+1][indexiJ])
							e.append(key[b+1][indexiJ])	
							flag=1
							break
			if flag==0:
				for v in range(5):
					if s[k] in key[v]:
						indexkI=v
						indexkJ=key[v].index(s[k])
						e.append(key[indexiI][indexkJ])
						e.append(key[indexkI][indexiJ])
						break
						
	flag=0					

print("This is Encrypted text %s"%e)			

s=e
p2=[]

for i in range(0,len(s)-1,2):
	k=i+1
	for j in range(0,5):
		if s[i] in key[j]:
			indexiI=j
			indexiJ=key[j].index(s[i])

			if s[k] in key[j]:
				indexkI=j
				indexkJ=key[j].index(s[k])
				p2.append(key[j][indexiJ-1])
				p2.append(key[j][indexkJ-1])
				flag=1

			else:
				for b in range(5):
					if s[k] == key[b][indexiJ]:
							p2.append(key[j-1][indexiJ])
							p2.append(key[b-1][indexiJ])	
							flag=1
							break
			if flag==0:
				for v in range(5):
					if s[k] in key[v]:
						indexkI=v
						indexkJ=key[v].index(s[k])
						p2.append(key[indexiI][indexkJ])
						p2.append(key[indexkI][indexiJ])
						break
						
	flag=0			
p2.remove("X")		
print("This is Decrypted text %s"%p2)