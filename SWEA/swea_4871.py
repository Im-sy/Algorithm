T = int(input())
def dfs():
    stack = []
    stack.append(start)
    visited = [0] * (V + 1)
    visited[start] = 1
    while stack:
        top = stack[-1]
        for i in range(1, V + 1):
            if arr[top][i] == 1 and not visited[i]:
                if i == end:
                    return 1
                stack.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()
    return 0

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        r, c = map(int, input().split())
        arr[r][c] = 1
    start, end = map(int, input().split())
    print(f'#{tc} {dfs()}')
