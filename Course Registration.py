# cook your dish here
for i in range(int(input())):
    N,M,K = map(int,input().split())
    if (abs(M-K) >= N):
        print("Yes")
    else:
        print("No")
