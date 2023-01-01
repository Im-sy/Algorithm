def nqueen(idx):
    global cnt
    if idx == N:
        cnt += 1
        return
    for i in range(N):
        if not col[i] and not dia1[idx+i] and not dia2[idx-i+N-1]:
            col[i] += 1
            dia1[idx+i] +=1
            dia2[idx-i+N-1] += 1
            nqueen(idx+1)
            col[i] -= 1
            dia1[idx + i] -= 1
            dia2[idx - i + N - 1] -= 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    col = [0]*N
    dia1 = [0]*(2*N-1)
    dia2 = [0]*(2*N-1)
    cnt = 0
    nqueen(0)
    print(f'#{tc} {cnt}')