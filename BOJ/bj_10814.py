N = int(input())
arr = [input().split() for _ in range(N)]
for i in range(len(arr)-1, 0, -1):
    for j in range(i):
        age = int(arr[j][0])
        age_next = int(arr[j+1][0])
        if age > age_next:
            arr[j], arr[j+1] = arr[j+1], arr[j]
for row in arr:
    print(row[0], row[1])