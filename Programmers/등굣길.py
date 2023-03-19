def solution(m, n, puddles):
    answer = 0
    maps = [[-1]*m for _ in range(n)]
    maps[0] = [1]*m
    for row in maps:
        row[0] = 1
    for [j, i] in puddles:
        maps[i - 1][j - 1] = 0
        if i-1 == 0:
            for jdx in range(j, m):
                maps[0][jdx] = 0
        if j-1 == 0:
            for idx in range(i, n):
                maps[idx][0] = 0
    print(maps)
    for i in range(1, n):
        for j in range(1, m):
            if maps[i][j] == 0:
                continue
            else:
                maps[i][j] = maps[i-1][j] + maps[i][j-1]
    answer = maps[n-1][m-1]
    return answer%1000000007


print(solution(4, 3, [[2, 2]]))
print(solution(4, 3, [[2, 2], [3, 3]]))
print(solution(4, 3, [[1, 2], [3, 3], [4, 1]]))
