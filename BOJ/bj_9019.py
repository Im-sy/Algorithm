def D(n):
    return (n*2) % 10000

def S(n):
    if n == 0:
        return 9999
    else:
        return n-1

def L(n):
    l = n % 1000
    r = n // 1000
    return l*10 + r

def R(n):
    l = n % 10
    r = n // 10
    return l*1000 + r

import sys
from collections import deque
T = int(input())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    q = deque()
    visited = set()
    q.append((A, ''))
    visited.add(A)
    while q:
        current, func = q.popleft()
        if current == B:
            print(func)
            break
        tmp = D(current)
        if tmp not in visited:
            visited.add(tmp)
            q.append((tmp, func+'D'))
        tmp = S(current)
        if tmp not in visited:
            visited.add(tmp)
            q.append((tmp, func + 'S'))
        tmp = L(current)
        if tmp not in visited:
            visited.add(tmp)
            q.append((tmp, func + 'L'))
        tmp = R(current)
        if tmp not in visited:
            visited.add(tmp)
            q.append((tmp, func + 'R'))