import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heights = list(map(int, input().split()))

l, r = 0, max(heights)
ans = 0

while l <= r:
    m = (l+r)//2
    res = sum(h-m if m<h else 0 for h in heights)
    if res >= M:
        ans = max(ans, m)
        l = m+1
    else:
        r = m-1

print(ans)