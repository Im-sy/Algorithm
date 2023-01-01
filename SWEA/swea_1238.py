import sys
sys.stdin = open('swea_1238.txt')

for tc in range(1, 11):
    N = 100
    M, V = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    edges = list(map(int, input().split()))
    for i in range(0, M, 2):
        s, e = edges[i], edges[i+1]
        arr[s][e] = 1
    visited = [0]*(N+1)
    queue = [V]
    visited[V] = 1
    while queue:
        front = queue.pop(0)
        for i in range(N+1):
            if arr[front][i] and not visited[i]:
                queue.append(i)
                visited[i] = visited[front] + 1
    max_tmp = max(visited)
    for i in range(N, -1, -1):
        if visited[i] == max_tmp:
            print(f'#{tc} {i}')
            break
