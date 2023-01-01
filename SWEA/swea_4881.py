T = int(input())

def permutation(idx, tmp_sum):
    global min_sum
    if idx == N:
        if min_sum > tmp_sum:
            min_sum = tmp_sum
        return
    if min_sum <= tmp_sum:
        return
    for i in range(N):
        if not used[i]:
            used[i] = 1
            permutation(idx+1, tmp_sum+arr[idx][i])
            used[i] = 0

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    min_sum = 9 * N
    permutation(0, 0)
    print(f'#{tc} {min_sum}')