import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse=True)
ans = 0
for i in range(N):
    ans += arr[i]*(i+1)
print(ans)