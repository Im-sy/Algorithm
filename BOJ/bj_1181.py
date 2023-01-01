N = int(input())
arr = [input() for _ in range(N)]
arr = list(set(arr))
print(arr)
for i in range(len(arr)-1, 0, -1):
    for j in range(i):
        if len(arr[j]) > len(arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]
        elif len(arr[j]) == len(arr[j+1]):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
print('\n'.join(arr))