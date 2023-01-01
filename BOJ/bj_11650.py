N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(len(arr)-1, 0, -1):
    for j in range(i):
        if arr[j][0] > arr[j+1][0]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        elif arr[j][0] == arr[j+1][0]:
            if arr[j][1] > arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
for xy in arr:
    print(' '.join(map(str, xy)))