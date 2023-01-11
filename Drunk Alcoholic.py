t = int(input())
for i in range(t):
    k = int(input())
    ans = 0
    for i in range(1,k+1):
        if i%2==1:
            ans+=3
        else:
            ans-=1
    print(ans)
    # if k%2!=0:
    #     print(k+2)
    # else:
    #     print(k+1)
