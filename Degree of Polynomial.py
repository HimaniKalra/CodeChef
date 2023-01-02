for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    
    for i in reversed(range(0,n)):
        if ls[i] != 0:
            print(i)
            break
