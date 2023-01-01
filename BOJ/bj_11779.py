import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))

INF = float('INF')
graph = [INF]*(n+1)
path = [[] for _ in range(n+1)]

def dijkstra(start):
    q = []
    graph[start] = 0
    path[start] = [start]
    heapq.heappush(q, (0, start, path[start]))
    while q:
        d, now, p = heapq.heappop(q)
        if graph[now] < d:
            continue
        for next, val in edges[now]:
            if graph[next] > d + val:
                graph[next] = d + val
                path[next] = p + [next]
                heapq.heappush(q, (d+val, next, path[next]))

start, end = map(int, input().split())
dijkstra(start)
print(graph[end])
print(len(path[end]))
print(*path[end])
