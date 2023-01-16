import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    q = deque([(r, c)])
    v = [(r, c)]
    while q:
        cr, cc = q.popleft()
        if cr == er and cc == ec:
            return "happy"
        for pr, pc in path:
            d = abs(cr-pr) + abs(cc-pc)
            if d <= 1000 and (pr, pc) not in v:
                q.append((pr, pc))
                v.append((pr, pc))
    return "sad"

t = int(input())
for _ in range(t):
    path = []
    n = int(input())
    sr, sc = map(int, input().split())
    for _ in range(n):
        con_r, con_c = map(int, input().split())
        path.append((con_r, con_c))
    er, ec = map(int, input().split())
    path.append((er, ec))
    print(bfs(sr, sc))