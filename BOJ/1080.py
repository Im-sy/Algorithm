import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().rstrip())) for _ in range(N)]
B = [list(map(int, input().rstrip())) for _ in range(N)]

def transfer(r, c):
    for i in range(r, r+3):
        for j in range(c, c+3):
            if A[i][j]:
                A[i][j] = 0
            else:
                A[i][j] = 1

cnt = 0
for r in range(N-2):
    for c in range(M-2):
        if A[r][c] != B[r][c]:
            transfer(r, c)
            cnt += 1

for r in range(N):
    for c in range(M):
        if A[r][c] != B[r][c]:
            cnt = -1

print(cnt)