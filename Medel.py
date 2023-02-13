for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = max(a)
    c = min(a)
    for i in a:
        if i == b or i == c:
            print(i, end=' ')
    print()
