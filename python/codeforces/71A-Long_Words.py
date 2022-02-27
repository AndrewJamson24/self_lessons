n = int(input(""))
x = 0
b = []
while x < n:
    w = list(input(""))

    if len(w) > 10:
        a = []
        a.append(w[0])
        a.append(len(w)-2)
        a.append(w[-1])
        trans = ''.join([str(elem) for elem in a])
    else:
        trans = ''.join([str(elem) for elem in w])
    
    b.append(trans)
    x +=1
for i in b:
    print(i)
