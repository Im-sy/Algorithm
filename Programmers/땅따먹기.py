## 시간 초과
# from sys import setrecursionlimit
# setrecursionlimit(10**6)
#
#
# def solution(land):
#     answer = 0
#
#     def dfs(idx, stk, tmp):
#         nonlocal answer
#         if idx == len(land):
#             if answer < tmp:
#                 answer = tmp
#                 print(stk)
#             return
#         for i in range(len(land[idx])):
#             if stk and stk[-1] == i:
#                 continue
#             stk.append(i)
#             dfs(idx + 1, stk, tmp + land[idx][i])
#             stk.pop()
#
#     dfs(0, [], 0)
#
#     return answer

def solution(land):
    answer = 0
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max([land[i-1][k] for k in range(4) if k != j])
    answer = max([land[i][j] for j in range(4)])
    return answer


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))