t=int(input())
for i in range(t):
    n,a,b,c=map(int,input().split())
    if n<=min(b,a+c):
        print("YES")
    else:
        print("NO")
        
