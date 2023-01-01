N, M = map(int, input().split())
ans = []
def permutation(start):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(start, N+1):
        ans.append(i)
        permutation(i)
        ans.pop()
permutation(1)