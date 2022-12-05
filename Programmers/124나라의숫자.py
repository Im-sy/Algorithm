n = int(input())

# 효율성 실패
# dp = ['0']*(n+1)
# dp[0] = '4'
# dp[1] = '1'
# if n >= 2:
#     dp[2] = '2'
# if n >= 3:
#     dp[3] = '4'
# for i in range(4, n+1):
#     if i%3:
#         dp[i] = str(dp[i//3]) + str(dp[i%3])
#     else:
#         dp[i] = str(dp[i//3 - 1]) + str(dp[i%3])
# print(dp[n])

def solve(n):
    if n == 1:
        return '1'
    if n == 2:
        return '2'
    if n == 3:
        return '4'
    if n % 3:
        return solve(n//3) + solve(n%3)
    else:
        return solve(n//3-1) + solve(n%3+3)

print(solve(n))