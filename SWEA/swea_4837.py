T = int(input())
arr = [x for x in range(1, 13)]
# 부분집합 미리 구해두기
subset = []
for i in range(1 << 12):
    tmp = []
    for j in range(12):
        if i & (1 << j):
            tmp.append(arr[j])
    subset.append(tmp)

for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    for x in subset:
        tmp_sum = 0
        if len(x) == N: # 길이가 N
            for n in x:
                tmp_sum += n
            if tmp_sum == K: # 합이 K
                cnt += 1
    print(f'#{tc} {cnt}')