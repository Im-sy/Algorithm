import sys
sys.stdin = open('swea_1219.txt')

for _ in range(10):
    tc, V = map(int, input().split())
    arr = list(map(int, input().split()))
    edge = [[-1]*100 for _ in range(2)]
    visited = [0]*100
    for i in range(0, V*2, 2):
        if edge[arr[i]][0] == -1:
            edge[0][arr[i]] = arr[i+1]
        else:
            edge[1][arr[i]] = arr[i+1]
    stack = []
    visited[0] = 1
    stack.append(0)
    ans = 0
    while stack:
        top = stack[-1]
        if top == 99:
            ans = 1
            break
        for i in range(2):
            if edge[i][top] != -1 and not visited[edge[i][top]]:
                stack.append(edge[i][top])
                visited[edge[i][top]] = 1
                break
        else:
            stack.pop()
    print(f'#{tc} {ans}')