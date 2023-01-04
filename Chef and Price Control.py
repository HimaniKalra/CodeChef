for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    s=0
    for i in l:
        if i>k:
            s=s+(i-k)
    print(s)
        
