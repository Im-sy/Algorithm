arr = [1, 2, 3, 4]
N = 4
used = [0]*N
def permutation(idx):
    if idx==N:
        print(arr)
        return
    for i in range(idx, N):
        arr[idx], arr[i] = arr[i], arr[idx]
        permutation(idx+1)
        arr[idx], arr[i] = arr[i], arr[idx]
permutation(0)

new_arr = [0]*N
def permutation2(idx):
    if idx==N:
        print(new_arr)
        return
    for i in range(N):
        if not used[i]:
            used[i] = 1
            permutation2(idx+1)
            used[i] = 0
permutation2(0)