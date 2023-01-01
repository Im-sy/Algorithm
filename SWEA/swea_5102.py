# def bfs(S, G):
#     queue = [(S, 0)]
#     visited = [0]*(V+1)
#     visited[S] = 1
#     while queue:
#         front, distance = queue.pop(0)
#         if front == G:
#             return distance
#         for i in range(V+1):
#             if arr[front][i] and not visited[i]:
#                 queue.append((i, distance+1))
#                 visited[i] = 1
#     return 0
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     arr = [[0]*(V+1) for _ in range(V+1)]
#     for _ in range(E):
#         s, e = map(int, input().split())
#         arr[s][e] = 1
#         arr[e][s] = 1
#     S, G = map(int, input().split())
#     print(f'#{tc} {bfs(S, G)}')

def dfs(S, G):
    stack = [(S, 0)]
    visited = [0]*(V+1)
    visited[S] = 1
    while stack:
        top, distance = stack.pop()
        if top == G:
            return distance
        for i in range(V+1):
            if arr[top][i] and not visited[i]:
                stack.append((i, distance+1))
                visited[i] = 1
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        arr[s][e] = 1
        arr[e][s] = 1
    S, G = map(int, input().split())
    print(f'#{tc} {dfs(S, G)}')
