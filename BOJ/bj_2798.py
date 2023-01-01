N, M = map(int, input().split())
arr = list(map(int, input().split()))
max_sum = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            tmp_sum = arr[i] + arr[j] + arr[k]
            if max_sum < tmp_sum <= M:
                max_sum = tmp_sum
#245 36 216
print(max_sum)