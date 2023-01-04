t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    freq = {}
    for i in arr:
        freq[i] = freq.get(i,0) + 1
    max_freq = max(freq.values())
    print(len(arr)-max_freq)
