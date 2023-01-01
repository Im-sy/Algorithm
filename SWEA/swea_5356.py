T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    max_len = 0
    for x in arr:
        if max_len < len(x):
            max_len = len(x)
    print(f'#{tc}', end=' ')
    for j in range(max_len):
        i = 0
        while i < 5:
            try:
                print(arr[i][j], end='')
                i += 1
            except:
                i += 1
    print()