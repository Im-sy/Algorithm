import sys
N = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
ans = 0
midx = 0
for i in range(N-1):
    if price[midx] > price[i]:
        midx = i
    ans += price[midx]*length[i]
print(ans)