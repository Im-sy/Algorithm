import sys
def permutation(idx, perm, selected):
    if idx == M:
        print(*perm)
        # print(' '.join(list(map(str, perm))))
        return
    for i in range(N):
        if not selected[i]:
            perm[idx] = arr[i]
            selected[i] = 1
            permutation(idx+1, perm, selected)
            selected[i] = 0


N, M = map(int, sys.stdin.readline().split())
arr = list(range(1, N+1))
permutation(0, [0]*M, [0]*(N+1))


result = []
def perm():
    if len(result) == M:
        print(' '.join(list(map(str, result))))
        return
    for i in range(1, N + 1):
        if i not in result:
            result.append(i)
            perm()
            result.pop()


