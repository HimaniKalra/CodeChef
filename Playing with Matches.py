for _ in range(int(input())):
    a,b = map(int, input().split())
    c=str(a+b)
    sticks=0
    for i in range(len(c)):
        n=c[i]
        if n=='0' or n=='6'or n=='9':
            sticks = sticks + 6
        elif n=='2' or n=='3'or n=='5':
            sticks = sticks + 5
        elif n=='1':
            sticks = sticks + 2
        elif n=='4':
            sticks = sticks + 4
        elif n=='7':
            sticks = sticks + 3
        elif n=='8':
            sticks = sticks + 7
    
    print(sticks)
