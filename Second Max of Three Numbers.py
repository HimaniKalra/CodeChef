for _ in range(int(input())):
    a,b,c = list(map(int, input().split()))
    if a >= b and a >= c:
        print(max(b,c))
    elif b >= a and b >= c:
        print(max(a,c))
    else:
        print(max(b,a))
