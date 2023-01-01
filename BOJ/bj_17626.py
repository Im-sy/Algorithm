N = int(input())
dp = [0, 1]
for i in range(2, N+1):
    min_tmp = 10**9
    j = 1
    while j**2 <= i:
        min_tmp = min(min_tmp, dp[i - j**2])
        j += 1
    dp.append(min_tmp+1)
print(dp[N])
'''
N = 10
dp[0] = 0
dp[1] = 1 / 1^2 
dp[2] = 2 / 1^2 + 1^2
dp[3] = 3 / 1^2 + 1^2 + 1^2
dp[4] = 1 / 2^2
dp[5] = 2 / 2^2 + 1^2
dp[6] = 3 / 2^2 + 1^2 + 1^2
dp[7] = 4 / 2^2 + 1^2 + 1^2 + 1^2
dp[8] = 2 / 2^2 + 2^2
dp[9] = 1 / 3^3
dp[10] = 2 / 3^3 + 1^2 
'''