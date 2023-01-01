import sys
input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sum_list = [0]
tmp_sum = 0
for num in numbers:
    tmp_sum += num
    sum_list.append(tmp_sum)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_list[j]-sum_list[i-1])