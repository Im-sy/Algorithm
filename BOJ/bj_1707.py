import sys

# 재귀 사용하는 경우
# def dfs(v, group):
#     visited[v] = group
#     for i in arr[v]:
#         if not visited[i]:
#             if not dfs(i, -group):
#                 return False
#         elif visited[i] == visited[v]:
#             return False
#     return True

# stack 사용하는 경우
# visited를 1과 -1로 구분해서 이분 그래프인지 판단
def mydfs(v):
    stack = [v]
    visited[v] = 1
    while stack:
        current = stack.pop()
        # for i in range(1, V + 1):
        #     if arr[current][i]:
        
        # current에 연결되어있는 값들
        for i in arr[current]:
            # 아직 방문하지 않은 경우
            if not visited[i]:
                stack.append(i)
                # current와 다른 그룹으로 분류
                visited[i] = -1 * visited[current]
            # 방문했는데 current와 같은 그룹이라면 이분 그래프 아님
            elif visited[current] == visited[i]:
                return False
    else: # 정상적으로 탐색 마치면 이분 그래프
        return True


T = int(sys.stdin.readline())
for tc in range(1, T+1):
    V, E = map(int, sys.stdin.readline().split())
    # 메모리 초과 (인접행렬)
    # arr = [[0]*(V+1) for _ in range(V+1)]
    # for _ in range(E):
    #     s, e = map(int, sys.stdin.readline().split())
    #     arr[s][e] = 1
    #     arr[e][s] = 1
    
    # 연결된 노드 저장
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, sys.stdin.readline().split())
        arr[s].append(e)
        arr[e].append(s)
        
    visited = [0]*(V+1)
    # 연결되지 않은 그래프 있을 수 있으니까 모든 노드 확인 필요
    for i in range(1, V+1):
        # 방문하지 않은 노드에 대해서
        if not visited[i]:
            # DFS 수행했는데 한 번이라도 실패하면 NO
            if not mydfs(i):
                print('NO')
                break
    else: # 모든 경우에 성공 시 YES
        print('YES')

    # for i in range(1, V+1):
    #     if not visited[i]:
    #         result = dfs(i, 1)
    #         if not result:
    #             break
    # print('YES' if result else 'NO')