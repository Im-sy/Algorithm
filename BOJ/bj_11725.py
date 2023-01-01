import sys

N = int(sys.stdin.readline())
# 연결 노드 저장
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

# DFS 수행
stack = [1]
visited = [0]*(N+1)
visited[1] = 1
while stack:
    current = stack.pop()
    # current와 연결된 노드들에 대해
    for i in arr[current]:
        if not visited[i]:
            stack.append(i)
            # 연결된 노드의 방문배열값에 current(부모)노드 저장
            visited[i] = current
for i in range(2, N+1):
    print(visited[i])