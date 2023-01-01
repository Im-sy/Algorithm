import sys
import heapq
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = float('INF')
dist = [INF]*(N+1)
def dijkstra(start):
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

start, end = map(int, input().split())
dijkstra(start)
print(dist[end])