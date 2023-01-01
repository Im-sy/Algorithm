from collections import deque

N, K = map(int, input().split())
ans = 100000
cnt = 0

def solve(n):
    global ans, cnt
    q = deque()
    q.append((n, 0))
    v = [0]*100001
    while q:
        now, d = q.popleft()
        # 1->2 경우에 +1도 되고, *2도 되기 떄문에 방문 처리를 pop때 해주자
        v[now] = 1
        if now == K and ans >= d:
            ans = d
            cnt += 1
        for nc in [now-1, now+1, now*2]:
            if 0<=nc<=100000 and not v[nc]:
                q.append((nc, d+1))

solve(N)
print(ans)
print(cnt)