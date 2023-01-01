#노드의 대표자 노드를 반환하는 함수
def find_set(x):
    # 스스로가 부모인 노드가 대표자 노드
    if p[x] == x:
        return x
    # 스스로 부모가 아니라면....부모의 대표자를 찾아 봐야 합니다.
    else:
        return find_set(p[x])


# 두 노드를 하나의 집합으로 만들어주는 함수
# (두 노드의 대표자를 하나로 만들기)
def union(a, b):
    p_a = find_set(a)
    p_b = find_set(b)
    # b의 대표자의 부모를 스스로가 아닌
    # a의 대표자로 만들어준다.
    p[p_b] = p_a


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     x_lst = list(map(int, input().split()))
#     y_lst = list(map(int, input().split()))
#     E = float(input())
#     edges = []
#     for i in range(N):
#         for j in range(N):
#             dist = ((x_lst[i]-x_lst[j])**2+(y_lst[i]-y_lst[j])**2)*E
#             edges.append((dist, i, j))
#     edges.sort()
#     p = list(range(N))
#     ans = 0
#     for edge in edges:
#         dist, i, j  = edge
#         if find_set(i) != find_set(j):
#             union(i, j)
#             ans += dist
#     print(f'#{tc} {round(ans)}')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    E = float(input())
    INF = 0xffffffffff
    arr = [[INF] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dist = ((x_lst[i] - x_lst[j]) ** 2 + (y_lst[i] - y_lst[j]) ** 2) * E
            arr[i][j] = dist
            arr[j][i] = dist

    group = [0]*N
    group[0] = 1
    weight = arr[0][:]
    weight[0] = 0
    result = 0
    for _ in range(N-1):
        min_v = INF
        min_idx = 0
        for i in range(N):
            if weight[i] < min_v and not group[i]:
                min_v = weight[i]
                min_idx = i
        group[min_idx] = 1
        result += min_v
        for i in range(N):
            if weight[i] > arr[min_idx][i] and not group[i]:
                weight[i] = arr[min_idx][i]
    print(f'#{tc} {round(result)}')