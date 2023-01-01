N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
ans = []
# visited = [0]*N
def permutation(idx):
    if idx == M:
        print(*ans)
        return
    for i in range(N):
        if numbers[i] not in ans:
        # if not visited[i]:
        #     visited[i] = 1
            ans.append(numbers[i])
            permutation(idx+1)
            # visited[i] = 0
            ans.pop()
permutation(0)