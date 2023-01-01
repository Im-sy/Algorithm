T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x:x[1])
    # print(arr)
    j = 0
    result = [j]
    for i in range(1, N):
        if arr[j][1] <= arr[i][0]:
            result.append(i)
            j = i
    print(f'#{tc} {len(result)}')