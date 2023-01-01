import sys, heapq

def find_set(x):
    if p[x] == x:
        return x
    else:
        return find_set(p[x])

def union(a, b):
    p_a = find_set(a)
    p_b = find_set(b)
    p[p_b] = p_a

V, E = map(int, sys.stdin.readline().split())
INF = 0xffffffff
# edges = [[] for _ in range(V+1)]
data = []
for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().split())
    # edges[s].append((e, w))
    # edges[e].append((s, w))
    heapq.heappush(data, (w, s, e))
p = [x for x in range(V+1)]
def kruskal(data):
    ans = 0
    while data:
        w,s,e = heapq.heappop(data)
        if find_set(s) == find_set(e):
            continue
        ans += w
        union(s, e)
    return ans

result = kruskal(data)

print(result)



# def prim(start):
#     D = edges[start][:]
#     D[start] = 0
#     U = [0] * (V+1)
#     U[start] = 1
#     weight = 0
#     for _ in range(V):
#         min_idx = 0
#         min_val = INF
#         for i in range(V+1):
#             if not U[i] and D[i] < min_val:
#                 min_idx = i
#                 min_val = D[i]
#         U[min_idx] = 1
#         weight += min_val
#         for i in range(V+1):
#             if not U[i] and edges[min_idx][i] < D[i]:
#                 D[i] = edges[min_idx][i]
#     return weight
#
# print(prim(1))

# U = [0]*(V+1)
# D = [(1, 0)]
# ans = 0
# cnt = 0
# while D:
#     if cnt == V:
#         break
#     c, w = heapq.heappop(D)
#     if not U[c]:
#         U[c] = 1
#         ans += w
#         cnt += 1
#         for i in edges[c]:
#             if not U[i[0]]:
#                 heapq.heappush(D, i)
# print(ans)



