import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

def permutation(idx, perm):
    if len(perm) == M:
        print(*perm)
        return
    tmp = 0
    for i in range(idx, N):
        if tmp != numbers[i]:
            perm.append(numbers[i])
            tmp = numbers[i]
            permutation(i, perm)
            perm.pop()

permutation(0, [])
