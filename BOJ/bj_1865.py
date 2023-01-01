import sys
input = sys.stdin.readline

INF = 1e9
def bellman_ford(start):
    graph = [INF]*(N+1)
    graph[start] = 0
    for i in range(N):
        for now, next, d in roads:
            # graph[now] != INF 조건은 시작점으로부터 이어진 노드의 최소거리 구하기 위함
            # 시작점과 관계없이 진행하면 graph는 최단거리 테이블이 아니라 음수 싸이클 존재 유무 판단 테이블
            # N번째 루프까지 갱신된다면 음수 싸이클
            if graph[next] > graph[now] + d:
                graph[next] = graph[now] + d
                if i == N-1:
                    return True
    return False

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    roads = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        roads.append((S, E, T))
        roads.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        roads.append((S, E, -T))

    # ans = 0
    # for i in range(1, N+1):
    #     if bellman_ford(i):
    #         ans = 1
    #         break
    # if ans:
    #     print('YES')
    # else:
    #     print('NO')
    if bellman_ford(1):
        print('YES')
    else:
        print('NO')