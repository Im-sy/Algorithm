def selectionsort(idx):
    if idx == n:
        return
    mmin = idx
    for i in range(idx+1, n):
        if arr[i] < arr[mmin]:
            mmin = i
    arr[mmin], arr[idx] = arr[idx], arr[mmin]
    selectionsort(idx+1)


arr = [3, 5, 1, 2, 4]
n = len(arr)
selectionsort(0)
print(arr)