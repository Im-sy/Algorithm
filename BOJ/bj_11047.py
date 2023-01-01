import sys
N, K = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort(reverse=True)
ans = 0
for x in arr:
    if x > K:
        continue
    if K == 0:
        break
    ans += K//x
    K %= x

print(ans)
