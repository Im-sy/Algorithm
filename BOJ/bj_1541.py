import sys
arr = list(input().split('-'))
# print(int('00009'))
for i in range(len(arr)):
    if '+' in arr[i]:
        arr[i] = sum(list(map(int, arr[i].split('+'))))
    else:
        arr[i] = int(arr[i])
ans = arr[0]
for i in range(1, len(arr)):
    ans -= arr[i]
print(ans)