import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    ans = [0]*(N+1)

    ans[1] = 1
    if N >= 2:
        ans[2] = 1
    for i in range(3, N+1):
        ans[i] = ans[i-3] + ans[i-2]

    # N이 1~5일때 조심하자..
    if N in [1, 2, 3]:
        print(1)
        continue
    elif N in [4, 5]:
        print(2)
        continue
    ans[1] = ans[2] = ans[3] = 1
    ans[4] = ans[5] = 2
    for i in range(6, N + 1):
        ans[i] = ans[i - 5] + ans[i - 1]

    print(ans[N])