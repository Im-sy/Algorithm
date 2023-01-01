N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
ans = []
def permutation(idx):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(idx, N):
        ans.append(numbers[i])
        permutation(i)
        ans.pop()
permutation(0)