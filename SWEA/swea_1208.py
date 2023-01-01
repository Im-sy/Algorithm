for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    idx_min = idx_max = 0
    while N >= 0:
        tmp_min = 101
        tmp_max = 0
        for i in range(100):
            if arr[i] < tmp_min:
                tmp_min = arr[i]
                idx_min = i
            if arr[i] > tmp_max:
                tmp_max = arr[i]
                idx_max = i
        if N == 0:
            print(f'#{tc} {arr[idx_max] - arr[idx_min]}')
        else:
            arr[idx_min] += 1
            arr[idx_max] -= 1
        N -= 1