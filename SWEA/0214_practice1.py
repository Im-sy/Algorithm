arr = [list(map(int,input().split())) for _ in range(5)]
dr = [-1, 0, 1, 0] #상우하좌
dc = [0, 1, 0, -1]
tmp_sum = 0
for i in range(5):
    for j in range(5):
        for k in range(4):
            ni = i+dr[k]
            nj = j+dc[k]
            if 0<=ni<5 and 0<=nj<5:
                tmp_sum += abs(arr[ni][nj]-arr[i][j])
print(tmp_sum)