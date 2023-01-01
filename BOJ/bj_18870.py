N = int(input())
arr = list(map(int, input().split()))
arr2 = []
for i in arr:
    if i not in arr2:
        arr2.append(i)
cnt = {}
for i in range(len(arr2)):
    for j in range(len(arr2)):
        if i != j:
            if arr2[i] > arr2[j]:
                cnt[arr2[i]] = 1
            else:
                cnt[arr2[i]] = 0
for x in arr:
    print(cnt[x], end=' ')