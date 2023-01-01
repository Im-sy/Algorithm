from collections import deque
A, B = map(int, input().split())

def solve(n):
    q = deque()
    q.append((n, 1))
    while q:
        now, d = q.popleft()
        if now == B:
            return d
        if 2*now<=B:
            q.append((2*now, d+1))
        plus_one = 10*now+1
        if plus_one<=B:
            q.append((plus_one, d+1))
    return -1

print(solve(A))