import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

v = [0]*N
ans = []
def permutation(idx):
    if idx == M:
        print(*ans)
        return
    tmp = 0
    for i in range(N):
        if not v[i] and tmp != numbers[i]:
            v[i] = 1
            ans.append(numbers[i])
            tmp = numbers[i]
            permutation(idx+1)
            v[i] = 0
            ans.pop()

permutation(0)
print('============')
def permutate(idx, perm, sel):
    if idx == M:
        print(*perm)
        return
    tmp = 0
    for i in range(N):
        if not sel[i] and tmp != numbers[i]:
            sel[i] = 1
            perm.append(numbers[i])
            tmp = numbers[i]
            permutate(idx+1, perm, sel)
            sel[i] = 0
            perm.pop()
permutate(0, [], [0]*N)