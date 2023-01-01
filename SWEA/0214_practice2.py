arr = list(map(int, input().split()))
n = len(arr)
for i in range(1<<n):
    tmp_sum = 0
    subset = []
    for j in range(i):
        if i & (1<<j):
            tmp_sum += arr[j]
            subset.append(arr[j])
    if tmp_sum == 10:
        print(subset, end=' ')

# 재귀함수 사용해서 부분집합 구하기
bit = [0]*n
def ps(idx):
    if idx==n:
        for i in range(n):
            if bit[i]:
                print(arr[i], end=' ')
        print()
        return
    # bit의 idx 번째 요소에0 또는 1 넣어주기
    for i in range(2):
        bit[idx] = i
        ps(idx+1)
    # bit[idx] = 0
    # ps(idx+1)
    # bit[idx] = 1
    # ps(idx+1)
ps(0)