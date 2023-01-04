for _ in range(int(input())):
    N=int(input())
    if N%7==6:
        print(N//7 + 1)
    else:
        print(N//7)
