import sys
input = sys.stdin.readline

N, C = map(int, input().split())
homes = sorted([int(input().strip()) for _ in range(N)])

l = 1
r = homes[N-1] - homes[0]
ans = 0

while l<=r:
    m = (l+r)//2
    tmp = homes[0]
    cnt = 1
    for i in range(1, N):
        if homes[i] - tmp >= m:
            cnt += 1
            tmp = homes[i]
    if cnt >= C:
        ans = m
        l = m+1
    else:
        r = m-1

print(ans)
