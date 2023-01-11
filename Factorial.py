t = int(input())
for t in range(t):
    x = int(input())
    d = 5
    z = 0
    while(d<=x):
        z += int(x/d)
        d = d*5
    print(z)
