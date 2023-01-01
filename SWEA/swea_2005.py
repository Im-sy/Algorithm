T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    arr[0][0] = 1
    for r in range(1, N):
        arr[r][0] = 1
        for c in range(1, N):
            arr[r][c] = arr[r-1][c-1] + arr[r-1][c]
    print(f'#{tc}')
    for r in range(N):
        for c in range(N):
            if arr[r][c]:
                print(arr[r][c], end=' ')
        print()

# 교수님 풀이
arr = [[0] * 10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        if j == 0 or i == j:
            arr[i][j] = 1
        elif j > i:
            continue
        else:
            arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1]
for tc in range(1, T+1):
    N = int(input())
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j], end=' ')
        print()

