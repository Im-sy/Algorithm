T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    max_tmp = arr[-1]
    for i in range(N-1, -1, -1):
        if arr[i] > max_tmp:
            max_tmp = arr[i]
        result += max_tmp - arr[i]
    print(f'#{tc} {result}')