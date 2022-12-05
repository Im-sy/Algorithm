import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    scores.sort(key=lambda x:[x[0], x[1]])
    ans = 1
    interview = scores[0][1]
    for i in range(1, N):
        if scores[i][1] < interview:
            ans += 1
            interview = scores[i][1]
    print(ans)
