import sys
V = int(sys.stdin.readline())

# 인접행렬 저장
edges = [[] for _ in range(V+1)]
for _ in range(V):
    info = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(info), 2):
        if info[i] == -1:
            break
        else:
            # info[i] : 정점번호, info[i+1] : 정점까지 거리
            edges[info[0]].append((info[i], info[i+1]))
# print(edges)

# dfs 수행
# visited 배열에 현재까지의 거리 누적합 저장
# 거리가 가장 먼 점(인덱스), 가장 먼 거리-1 반환
# 처음에 거리 기본값 1로 주었기 때문에 -1 필요
def dfs(n):
    stack = [n]
    visited = [0]*(V+1)
    visited[n] = 1
    while stack:
        current = stack.pop()
        for i in range(len(edges[current])):
            if edges[current][i][0] and not visited[edges[current][i][0]]:
                stack.append(edges[current][i][0])
                visited[edges[current][i][0]] = visited[current] + edges[current][i][1]
    return visited.index(max(visited)), max(visited)-1

# 아무 점에서 가장 먼 점 a 구하고, a에서 다시 가장 먼 점 b 구하면
# a와 b 사이 거리가 트리의 지름!
a, d1 = dfs(1)
b, d2 = dfs(a)
print(d2)
