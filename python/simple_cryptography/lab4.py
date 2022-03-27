from random import randint
key_p = []
for i in range(64):
	key_p += str(randint(0, 1))
print("Cheie este: " + "".join(key_p))


middle_index = len(key_p) // 2 
 
C = key_p[:middle_index] 
D = key_p[middle_index:]

print("C: "+"".join(C))
print("D: "+"".join(D))
 


i = int(input("A cata iteratie doriti? (1<=i<=16): "))
while True:
    if i >= 1 and i <= 16:
        for a in range (1,i+1):
            if (i==1 or i==2 or i==9 or i==16):
                C.append(C.pop(0))
                D.append(D.pop(0))
            else: 
                C.append(C.pop(0))
                C.append(C.pop(0))
                D.append(D.pop(0))
                D.append(D.pop(0))
        print("C: "+"".join(C))
        print("D: "+"".join(D))
        break
    else:
        i = int(input("Introduceti i in diapazonul 1-16: "))


