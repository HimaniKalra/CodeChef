T = int(input())
for i in range(T):
    X,Y,Z=map(int,input().split())
    A = (Z-Y)//X
    print(A)
