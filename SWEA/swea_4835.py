T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    tmp = 0
    for i in range(M):
        tmp += arr[i]
    tmp_max = tmp_min = tmp
    for i in range(1, N-M+1):
        tmp_sum = 0
        for j in range(M):
            tmp_sum += arr[i+j]
        if tmp_sum < tmp_min:
            tmp_min = tmp_sum
        if tmp_sum > tmp_max:
            tmp_max = tmp_sum
    print(f'#{tc} {tmp_max-tmp_min}')