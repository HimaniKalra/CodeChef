for _ in range(int(input())):
    a,b=map(int,input().split())
    if b%a==0:
        print((b//a)-1)
    else:
        print(b//a)
