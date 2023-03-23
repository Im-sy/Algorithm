def solution(triangle):
    answer = 0
    dp = triangle.copy()
    for i in range(1, len(triangle)):
        for j in range(0, i+1):
            if j == 0:
                dp[i][j] += triangle[i-1][j]
                continue
            if j == i:
                dp[i][j] += triangle[i-1][j-1]
                continue
            dp[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    answer = max(dp[-1])
    # print(dp)
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))