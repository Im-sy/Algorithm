import sys
import heapq
input = sys.stdin.readline
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = float('INF')
def dijkstra(start):
    dist = [INF]*(N+1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, val in graph[now]:
            if dist[next] > d+val:
                dist[next] = d+val
                heapq.heappush(q, (d+val, next))
    return dist

ans = 0
back = dijkstra(X)
for i in range(1, N+1):
    go = dijkstra(i)
    # print(go, back, go[X]+back[i])
    ans = max(ans, go[X]+back[i])
print(ans)