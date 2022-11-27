n=int(input())
for i in range(n):
    a,b=list(map(int,input().split()))
    if a>0 and b>0:
        if a==b:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
