import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]

max_dp = deepcopy(numbers[0])
min_dp = deepcopy(numbers[0])
max_tmp = [0]*3
min_tmp = [0]*3

for i in range(1, N):
    # max_tmp[0] = max(max_dp[0], max_dp[1]) + numbers[i][0]
    # max_tmp[1] = max(max_dp[0], max_dp[1], max_dp[2]) + numbers[i][1]
    # max_tmp[2] = max(max_dp[1], max_dp[2]) + numbers[i][2]
    # min_tmp[0] = min(min_dp[0], min_dp[1]) + numbers[i][0]
    # min_tmp[1] = min(min_dp[0], min_dp[1], min_dp[2]) + numbers[i][1]
    # min_tmp[2] = min(min_dp[1], min_dp[2]) + numbers[i][2]
    # for j in range(3):
    #     max_dp[j] = max_tmp[j]
    #     min_dp[j] = min_tmp[j]
    max_dp = [max(max_dp[0], max_dp[1]) + numbers[i][0],\
              max(max_dp[0], max_dp[1], max_dp[2]) + numbers[i][1],\
              max(max_dp[1], max_dp[2]) + numbers[i][2]]
    min_dp = [min(min_dp[0], min_dp[1]) + numbers[i][0],\
              min(min_dp[0], min_dp[1], min_dp[2]) + numbers[i][1],\
              min(min_dp[1], min_dp[2]) + numbers[i][2]]
# print(max_dp, min_dp)
print(max(max_dp), min(min_dp))
