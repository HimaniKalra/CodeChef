a,b,c = map(int, input().split())
d = list(map(int, input().split()))
for t in range(a):
    if (d[t]+c)>=b:
        print("YES")
        break
else:
    print("NO")
