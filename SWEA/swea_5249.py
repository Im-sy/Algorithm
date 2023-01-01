T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    INF = 0xfffffff
    arr = [[INF] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        arr[n1][n2] = w
        arr[n2][n1] = w

    group = [0]*(V+1)
    group[0] = 1
    weight = arr[0][:]
    weight[0] = 0
    for _ in range(V):
        min_v = INF
        min_idx = 0
        for i in range(V+1):
            if weight[i] < min_v and not group[i]:
                min_v = weight[i]
                min_idx = i
        group[min_idx] = 1
        for i in range(V+1):
            if weight[i] > arr[min_idx][i] and not group[i]:
                weight[i] = arr[min_idx][i]
    print(f'#{tc} {sum(weight)}')