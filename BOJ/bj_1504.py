import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

INF = float('INF')
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist = [INF]*(N+1)
    dist[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, val in edges[now]:
            if dist[next] > d+val:
                dist[next] = d+val
                heapq.heappush(q, (d+val, next))
    return dist

v1, v2 = map(int, input().split())
path_1 = dijkstra(1)
path_v1 = dijkstra(v1)
path_v2 = dijkstra(v2)
ans = min(path_1[v1]+path_v1[v2]+path_v2[N], path_1[v2]+path_v2[v1]+path_v1[N])
if ans < INF:
    print(ans)
else:
    print(-1)