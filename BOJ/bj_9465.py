import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(2)]
    if n >= 2:
        scores[0][1] += scores[1][0]
        scores[1][1] += scores[0][0]
        for i in range(2, n):
            scores[0][i] += max(scores[1][i-1], scores[1][i-2])
            scores[1][i] += max(scores[0][i-1], scores[0][i-2])
    print(max(scores[0][n-1], scores[1][n-1]))

# 50  40  200  140   250
# 30  100 120  210   260