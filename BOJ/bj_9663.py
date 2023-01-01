def nqueen(idx):
    global cnt
    if idx == N:
        cnt += 1
        return
    for i in range(N):
        if not col[i] and not dia1[idx+i] and not dia2[idx-i+N-1]:
            col[i] += 1
            dia1[idx+i] += 1
            dia2[idx-i+N-1] += 1
            nqueen(idx+1)
            col[i] -= 1
            dia1[idx + i] -= 1
            dia2[idx - i + N - 1] -= 1


def nqueens(idx):
    global ans
    if idx == N:
        ans += 1
        return
    for i in range(N):
        col[idx] = i
        for j in range(idx):
            if col[idx] == col[j] or abs(col[idx]-col[j])==abs(idx-j):
                break
        else:
            nqueens(idx+1)

# 제출 시 PyPy 사용하기
import sys
N = int(sys.stdin.readline())
col = [0]*N
dia1 = [0]*(2*N-1)
dia2 = [0]*(2*N-1)
cnt = 0
nqueen(0)
print(cnt)

ans = 0
nqueens(0)
print(ans)