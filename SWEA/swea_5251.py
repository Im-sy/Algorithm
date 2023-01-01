# 다익스트라

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    edges = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, d = map(int, input().split())
        edges[s][e] = d
    visited = [0]*(N+1)
    dist = [10000000]*(N+1)
    dist[0] = 0
    for _ in range(N+1):
        midx = -1
        tmp = 10000000
        for i in range(N+1):
            if not visited[i] and dist[i]<tmp:
                tmp = dist[i]
                midx = i
        visited[midx] = 1
        for i in range(N+1):
            if edges[midx][i] and not visited[i]:
                dist[i] = min(dist[i], dist[midx]+edges[midx][i])
    print(f'#{tc} {dist[N]}')