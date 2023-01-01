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

N = int(sys.stdin.readline())
arr = [list(map(float, sys.stdin.readline().split())) for _ in range(N)]
p = [_ for _ in range(N)]
data = []
for i in range(N):
    for j in range(N):
        if i != j:
            a = arr[i]
            b = arr[j]
            dist = round(((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5, 2)
            heapq.heappush(data, (dist, i, j))

def kruskal(data):
    ans = 0
    while data:
        w, s, e = heapq.heappop(data)
        if find_set(s) == find_set(e):
            continue
        ans += w
        union(s, e)
    return ans

print(kruskal(data))