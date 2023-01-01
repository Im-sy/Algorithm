# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 : 간선 정보
# 인접 행렬 만들기
N = 7
E = 8 # 간선 정보 개수
edges = list(map(int, input().split()))
adj = [[0]*(N+1) for _ in range(N+1)]
for i in range(0, E*2, 2): # 2개가 한 쌍
    a, b = edges[i], edges[i+1]
    adj[a][b] = 1
    adj[b][a] = 1
# for row in adj:
#     print(row)

# DFS 시작
# 1. 노드 방문
#   1-1. 방문 체크, 방문했던 노드는 재방문 X
#   1-2. 노드 번호 stack 에 넣기(stack push)
# 2. 현재 노드(stack top)에서 갈 수 있는 경로 탐색
#   2-1. 경로 발견 즉시 탐색종료 후 이동
#   2-2. 만약 갈 수 있는 경로 없으면 이전 경로로 되돌아감(stack pop)
# 1, 2번을 stack 빌 때까지 반복
stack = []
visited = [0]*(N+1)
start = 1
stack.append(start) # 시작점 1번 노드
visited[start] = 1 # 방문 표시
path = []
path.append(start)
while stack:
    current = stack[-1] # stack top
    for i in range(1, N+1):
        if adj[current][i] == 1 and not visited[i]: # current 와 연결됨 + 방문하지 않았음
            stack.append(i) # 경로 추가
            visited[i] = 1 # 방문 표시
            path.append(i)
            break
    else: # break 에 한 번도 안 걸렸다 => 갈 수 있는 길이 없다
        stack.pop()
print(path)