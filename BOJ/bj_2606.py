import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    arr[start][end] = 1
    arr[end][start] = 1

def dfs():
    visited = [0]*(N+1)
    stack = [1]
    visited[1] = 1
    # 1번과 연결된 컴퓨터 수
    cnt = 0
    while stack:
        current = stack[-1]
        for i in range(1, N+1):
            if arr[current][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                break
        else:
            # append 할 때 +1 하면 모든 경우에 대해서 카운트하게 됨
            # pop 할 때 +1 해주기
            stack.pop()
            cnt += 1
    # 1번은 포함하지 않으므로 하나 빼주기
    return cnt-1
print(dfs())