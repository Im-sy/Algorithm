from itertools import permutations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    perms = list(permutations(range(N)))
    ans = 0
    for perm in perms:
        tmp = 100
        for i in range(N):
            tmp *= arr[i][perm[i]]*(1/100)
        ans = max(tmp, ans)
    print(f'#{tc} {ans:.6f}')