import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

p = [0]*(n+1)
for i in range(1, n+1):
    p[i] = i

def find_p(p, x):
    if p[x] != x:
        p[x] = find_p(p, p[x])
    return p[x]

def union_p(p, a, b):
    a = find_p(p, a)
    b = find_p(p, b)
    if a<b:
        p[b] = a
    else:
        p[a] = b

for _ in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union_p(p, a, b)
    else:
        if find_p(p, a) == find_p(p, b):
            print('YES')
        else:
            print('NO')