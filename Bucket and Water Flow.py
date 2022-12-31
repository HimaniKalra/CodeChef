t=int(input())
for i in range(t):
    w,x,y,z=map(int,input().split())
    total = w + (y * z)
    if total==x:
        print("filled")
    elif total<x:
        print("Unfilled")
    else:
        print("overFlow")
