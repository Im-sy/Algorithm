import sys
sys.setrecursionlimit(10**6)


def solution(n):
    tile = [0]*n
    tile[0] = 1
    tile[1] = 2
    for i in range(2, n):
        tile[i] = (tile[i-2] + tile[i-1])%1000000007
    return tile[-1]%1000000007
    ## 시간 초과
    # if n == 1:
    #     return 1
    # if n == 2:
    #     return 2
    # return (solution(n-2) + solution(n-1))%1000000007

# n = 1 : 1
# n = 2 : 2
# n = 3 : 1 + 2 = 3
# n = 4 : 2 + 3 = 5


print(solution(4))