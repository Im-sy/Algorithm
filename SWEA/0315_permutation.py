arr = [1, 2, 3, 4]
N = 4
perm = [0]*N
used = [0]*N
# 새 배열의 idx 번째 자리에 어떤 숫자를 넣을지 결정
def solve(idx, perm, used):
    if idx == N:
        print(perm)
        return
    for i in range(N):
        if not used[i]:
            perm[idx] = arr[i]
            used[i] = 1
            solve(idx+1, perm, used)
            used[i] = 0

solve(0, perm, used)