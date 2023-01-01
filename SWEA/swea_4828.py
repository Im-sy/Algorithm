T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_tmp, min_tmp = arr[0]
    for x in arr:
        if max_tmp < x:
            max_tmp = x
        if min_tmp > x:
            min_tmp = x
    print(f'#{tc} {max_tmp - min_tmp}')