arr = list(range(1, 11))
N = 10

def powerset(selected, idx):
    if idx >= N:
        print(selected)
        tmp = 0
        subset = []
        for i in range(N):
            if selected[i] == 1:
                tmp += arr[i]
                subset.append(arr[i])
        if tmp == 10:
            print(subset)
    else:
        selected[idx] = 1
        powerset(selected, idx + 1)
        selected[idx] = 0
        powerset(selected, idx + 1)

