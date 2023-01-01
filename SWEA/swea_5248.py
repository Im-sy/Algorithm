def dfs(v):
    s = [v]
    visited[v] = 1
    while s:
        cv = s.pop()
        for i in range(N+1):
            if edges[cv][i] and not visited[i]:
                s.append(i)
                visited[i] = 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    edges = [[0]*(N+1) for _ in range(N+1)]
    vote = list(map(int, input().split()))
    for i in range(0, len(vote), 2):
        edges[vote[i]][vote[i+1]] = 1
        edges[vote[i+1]][vote[i]] = 1
    visited = [0]*(N+1)
    cnt = 0
    for x in range(1, N+1):
        if not visited[x]:
            dfs(x)
            cnt += 1
    print(f'#{tc} {cnt}')