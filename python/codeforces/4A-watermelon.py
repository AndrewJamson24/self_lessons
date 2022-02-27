x = int(input(" "))
q = []
k = []
r = []
if x >= 1 and x <= 100:
    for m in range(1,x):
        for n in range(1,m+1):
            if (m+n) == x :
                q.append(m)
                q.append(n)
    for i in q:
        if (i % 2) == 0:
            k.append(i)
    for m in k:
        for n in k:
            if (m+n) == x:
                r.append(x)
    if r:
        print("Yes")
    else:
        print("No")
else:
    print("The number should be between 1 -> 100")
