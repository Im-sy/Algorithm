import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lectures = list(map(int, input().split()))

def solve():
    cnt = 0
    tmp = 0
    for i in range(N):
        if tmp + lectures[i] > m:
            cnt += 1
            tmp = 0
        tmp += lectures[i]
    if tmp:
        cnt += 1
    return cnt

l = max(lectures)
r = sum(lectures)
while l <= r:
    m = (l+r) // 2
    tmp_cnt = solve()
    if tmp_cnt > M:
        l = m + 1
    else:
        r = m - 1

print(max(l, r, m))