N, K = map(int, input().split())
from collections import deque

# BFS 수행
q = deque()
v = [0]*100001
q.append((N, 0))
v[N] = 1
ans = 100000
while q:
    current, d = q.popleft()
    # 원하는 값에 도달했다면 가장 작은 값인지 확인하고 저장
    if current == K:
        if ans > d:
            ans = d
        break
    # 왼쪽, 오른쪽, 두배 위치 확인
    for nc in [current-1, current+1, current*2]:
        if 0<=nc<=100000 and not v[nc]:
            q.append((nc, d+1))
            v[nc] = 1

print(d)