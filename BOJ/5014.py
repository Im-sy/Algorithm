from collections import deque

F, S, G, U, D = map(int, input().split())

def bfs(s):
    q = deque([s])
    v = [0]*(F+1)
    v[s] = 1
    while q:
        cn = q.popleft()
        if cn == G:
            return v[cn]-1
        if 0<cn+U<=F and not v[cn+U]:
            q.append(cn+U)
            v[cn+U] = v[cn] + 1
        if 0<cn-D<=F and not v[cn-D]:
            q.append(cn-D)
            v[cn-D] = v[cn] + 1
    return "use the stairs"

print(bfs(S))