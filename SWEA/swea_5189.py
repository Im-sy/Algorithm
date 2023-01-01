def permutation(idx, perm, selected):
    global result
    if idx >= N-1:
        tmp = [0] + perm + [0]
        tmp_sum = 0
        for i in range(0, len(tmp)-1):
            tmp_sum += arr[tmp[i]][tmp[i+1]]
        if tmp_sum < result:
            result = tmp_sum
        return
    for i in range(N-1):
        if not selected[i]:
            perm[idx] = num[i]
            selected[i] = 1
            permutation(idx+1, perm, selected)
            selected[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num = [i for i in range(1, N)]
    result = 9999999
    permutation(0, [0]*(N-1), [0]*(N-1))
    print(f'#{tc} {result}')