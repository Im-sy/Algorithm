# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# 인접행렬로 저장
data = list(map(int, input().split()))
V = 7
E = 8
adj = [[0]*(V+1) for _ in range(V+1)]
for i in range(0, E*2, 2): # 2개가 한 쌍
    s, e = data[i], data[i+1]
    adj[s][e] = 1
    adj[e][s] = 1

# BFS 수행 (최단거리 계산)
visited = [0]*(V+1)
queue = []
queue.append(1) # 시작 정점
while queue:
    front = queue.pop(0)
    print(front, end=' ') # 방문 출력
    visited[front] = 1
    for i in range(1, V+1):
        # i번 노드에 방문 가능 => enqueue
        if adj[front][i] and not visited[i]:
            queue.append(i)
            # visited[i] = 1