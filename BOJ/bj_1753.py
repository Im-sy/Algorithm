# import sys
# input = sys.stdin.readline
# V, E = map(int, input().split())
# K = int(input())
# INF = float("INF")
# edges = [[INF]*(V+1) for _ in range(V+1)]
#
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     edges[u][v] = w
#
# def dijkstra(start):
#     D = edges[start][:]
#     U = {start}
#     while len(U)<V+1:
#         min_val = INF
#         min_idx = 0
#         for i in range(1, V):
#             if i not in U and D[i] < min_val:
#                 min_idx = i
#                 min_val = D[i]
#         U.add(min_idx)
#         for i in range(1, V+1):
#             if i not in U and D[i]>D[min_idx]+edges[min_idx][i]:
#                 D[i] = D[min_idx] + edges[min_idx][i]
#     return D
#
# weights = dijkstra(K)
# for i in range(1, V+1):
#     if weights[i] == INF:
#         print("INF")
#     else:
#         print(weights[i])


import sys
import heapq
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
INF = float("INF")
edges = [[] for _ in range(V+1)]
dist = [INF]*(V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for to, val in edges[now]:
            if dist[to] > d + val:
                dist[to] = d + val
                heapq.heappush(q, (d+val, to))

dijkstra(K)
for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])