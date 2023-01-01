import sys
import heapq
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
INF = float('INF')
# graph = [[INF]*(n+1) for _ in range(n+1)]
#
# for i in range(1, n+1):
#     graph[i][i] = 0
#
# for _ in range(r):
#     a, b, l = map(int, input().split())
#     graph[a][b] = l
#     graph[b][a] = l
#
# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
#
# ans = 0
# for i in range(1, n+1):
#     tmp = 0
#     for j in range(1, n+1):
#         if graph[i][j] <= m:
#             tmp += items[j]
#     ans = max(ans, tmp)
#
# print(ans)


edges = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    edges[a].append((b, l))
    edges[b].append((a, l))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    graph = [INF]*(n+1)
    graph[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if graph[now] < d:
            continue
        for next, val in edges[now]:
            if graph[next] > d+val:
                graph[next] = d+val
                heapq.heappush(q, (d+val, next))
    return graph

ans = 0
for i in range(1, n+1):
    tmp = 0
    res = dijkstra(i)
    for j in range(1, n+1):
        if res[j] <= m:
            tmp += items[j]
    ans = max(ans, tmp)

print(ans)