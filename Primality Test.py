from math import sqrt
for t in range(int(input())):
    n=int(input())
    flag=1
    if(n>1):
        for i in range(2,int(sqrt(n))+1):
            if(n%i==0):
                flag=0
        if(flag==0):
            print("no")
        else:
            print("yes")
    else:
        print("no")
