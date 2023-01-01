import sys

# dfs 수행
# tree인지 아닌지 판단 (싸이클인지 아닌지)
def dfs(v, prev):
    # 현재 노드 방문 표시
    visited[v] = 1
    # 현재 노드와 연결된 노드들에 대해서
    for next in arr[v]:
        # 인접행렬 저장 시 양방향으로 저장했기 때문에
        # 이전 노드랑 다음 노드랑 같으면 고려하지 않음
        if next == prev:
            continue
        # 다음 노드가 방문했던 점이면 싸이클(트리 아님)
        if visited[next]:
            return False
        # 다음 노드에서 dfs 수행해서 트리 아니면 트리 아님
        if not dfs(next, v):
            return False
    # 순환하지않고 잘 연결 되어 있으면 트리 
    return True

tc = 1
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n==0 and m==0:
        break
    # 인접행렬 저장(양방향)
    arr = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        arr[a].append(b)
        arr[b].append(a)
    
    visited = [0]*(n+1)
    cnt = 0
    # 1번 노드부터 방문하지 않은 경우에 dfs 수행 트리라면 카운트
    for i in range(1, n+1):
        if not visited[i]:
            if dfs(i, 0):
                cnt += 1
    
    if cnt == 0:
        print(f'Case {tc}: No trees.')
    elif cnt == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {cnt} trees.')
    tc += 1