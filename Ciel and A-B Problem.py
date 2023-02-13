# cook your dish here
a,b = map(int,input().split())
c = a-b
r = c%10
if r == 9:
    print(c-1)
else:
    print(c+1)
