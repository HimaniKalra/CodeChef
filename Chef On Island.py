t=int(input())
for i in range(t):
    a,w,x,y,z=map(int,input().split( ))
    k=a/x 
    l=w/y     
    b=min(l,k)
    if z<=b:
        print('YES')
    else:
        print('NO')
