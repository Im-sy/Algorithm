import sys
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[1], x[0]))
# print(arr)
idx = 0
ans = 1
for i in range(1, N):
    if arr[idx][1] <= arr[i][0]:
        ans += 1
        idx = i
print(ans)