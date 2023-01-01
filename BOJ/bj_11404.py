import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = float("INF")
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, val in graph[now]:
            if dist[next] > d + val:
                dist[next] = d + val
                heapq.heappush(q, (d+val, next))
for i in range(1, n+1):
    dist = [INF] * (n + 1)
    dijkstra(i)
    for j in range(1, n+1):
        if dist[j] == INF:
            print(0, end=' ')
        else:
            print(dist[j], end=' ')
    print()