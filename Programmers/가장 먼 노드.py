from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    q = deque([1])
    v = [0]*(n+1)
    v[1] = 1
    while q:
        node = q.popleft()
        for n in graph[node]:
            if not v[n]:
                q.append(n)
                v[n] = v[node] + 1
    answer = v.count(max(v))
    return answer


import heapq


def dijkstra(n, edge):
    inf = float('INF')
    q = []
    dist = [inf]*(n+1)
    graph = [[] for _ in range(n+1)]
    for s, e in edge:
        graph[s].append([e, 1])
        graph[e].append([s, 1])
    dist[1] = 0
    heapq.heappush(q, [1, 0])
    while q:
        now, d = heapq.heappop(q)
        if dist[now] < d:
            continue
        for nxt, c in graph[now]:
            cost = c + d
            if cost < dist[nxt]:
                dist[nxt] = cost
                heapq.heappush(q, [nxt, cost])
    return dist.count(max(dist[1:]))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
print(dijkstra(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
