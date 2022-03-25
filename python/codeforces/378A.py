a,b = input("").split()
a = int(a)
b = int(b)
if a <= 6 and a >= 1:
    if b <= 6 and b >=1 :
        p1 = 0
        p2 = 0
        d = 0
        for i in range(1,7):
            if abs(a - i) < abs(b - i):
                p1 +=1 
            elif abs(a - i) > abs(b - i):
                p2 +=1
            else:
                d +=1
print(p1,d,p2)
        
