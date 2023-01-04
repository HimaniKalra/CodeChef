for i in range(int(input())):
    n,l,x=map(int,input().split())
    if (n-l)<l:
        print((n-l)*x)
    else:
        print(l*x)
