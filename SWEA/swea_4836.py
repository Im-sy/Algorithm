T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    for _ in range(N):
        # 왼쪽 위 점 좌표, 오른쪽 위 점 좌표, 색깔
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                arr[r][c] += color # 해당되는 영역에 색깔 더해주기
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3: # 빨강(1) + 파랑(2) = 3
                cnt += 1
    print(f'#{tc} {cnt}')
