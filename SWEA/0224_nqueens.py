# 대각선1 = i+j
# 대각선2 = i-j+N-1
# 퀸 놓을 수 있는지 확인 위해서 배열 3개 사용
N = 5
col_check = [0]*N
dia1_check = [0]*(2*N-1)
dia2_check = [0]*(2*N-1)
cnt = 0
def nqueen(idx):
    global cnt
    if idx == N: # 모든 행에 퀸 놓았음
        cnt += 1
        return
    for i in range(N):
        if not col_check[i] and not dia1_check[idx+i] and not dia2_check[idx-i+N-1]:
            # 퀸 놓고, 영향 미치는 칸에 표시
            col_check[i] += 1
            dia1_check[idx+i] += 1
            dia2_check[idx-i+N-1] += 1
            nqueen(idx+1)
            # 퀸 빼고, 영향 미치는 칸 표시 지우기
            col_check[i] -= 1
            dia1_check[idx+i] -= 1
            dia2_check[idx-i+N-1] -= 1
nqueen(0)
print(cnt)