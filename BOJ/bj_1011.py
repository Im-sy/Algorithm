import sys
from collections import deque
input = sys.stdin.readline

def solve(s, e):
    q = deque([(1, 1, 1)])
    while q:
        k, cnt, tmp = q.popleft()
        if tmp == e-s-1:
            return cnt+1
        for i in [k-1, k, k+1]:
            q.append((i, cnt+1, tmp+i))

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    # print(solve(x, y))
    diff = int(y-x)
    if diff <= 3:
        print(diff)
    else:
        n = int(diff**(1/2))
        if diff == n**2:
            print(2*n-1)
        elif n**2 < diff <= n**2+n:
            print(2*n)
        else:
            print(2*n+1)