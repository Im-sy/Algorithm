edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
V = 7
adj = [[0]*(V+1) for _ in range(V+1)]
adj_list = [[] for _ in range(V+1)] # 인접 행렬
for i in range(0, len(edges),2):
    a, b = edges[i], edges[i+1]
    adj[a][b] = 1
    adj[b][a] = 1
    adj_list[a].append(b)
    adj_list[b].append(a)

def dfs():
    stack = []
    # 노드 방문하면 stack 경로 추가
    # 해당 경로에서 방문가능한 노드가 없으면 stack pop
    # stack의 모든 요소가 모두 삭제될 때 까지 반복
    visited = [0]*(V+1)
    stack.append(1)
    visited[1] = 1
    while stack:
        top = stack.pop()
        print(top, end=' ')
        for i in range(V+1):
            if adj[top][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
    print()
dfs()

visited = [0]*(V+1)
def dfs2(v):
    visited[v] = 1
    print(v, end=' ')
    for k in adj_list[v]:
        if not visited[k]:
            dfs2(k)
dfs2(1)

def bfs():
    queue = []
    visited = [0]*(V+1)
    queue.append(1)
    visited[1] = 1
    while queue:
        front = queue.pop(0)
        print(front, end=' ')
        for i in range(1, V+1):
            if adj[front][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1
    print()
bfs()