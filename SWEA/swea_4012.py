import sys
sys.stdin = open('swea_4012.txt')

# T = int(input())
# def synergy(lst):
#     result = 0
#     for r in range(N//2):
#         for c in range(r+1, N//2):
#             result += arr[lst[r]][lst[c]] + arr[lst[c]][lst[r]]
#     return result
#
# def dfs(idx, n):
#     global ans
#     if idx == N//2:
#         A = []
#         B = []
#         for i in range(N):
#             if visited[i]:
#                 A.append(i)
#             else:
#                 B.append(i)
#         result = abs(synergy(A)-synergy(B))
#         if result < ans:
#             ans = result
#         return
#
#     for i in range(n, N):
#         if not visited[i]:
#             visited[i] = 1
#             dfs(idx+1, n+1)
#             visited[i] = 0
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [0]*N
#     ans = 999999999
#     dfs(0, 0)
#     print(f'#{tc} {ans}')


# 유튜브라이브
def DFS(n, A, B):
    global ans
    if n == N:
        if len(A) == len(B):
            asum = bsum = 0
            for i in range(len(A)):
                for j in range(len(A)):
                    asum += arr[A[i]][A[j]]
                    bsum += arr[B[i]][B[j]]
            if ans > abs(asum-bsum):
                ans = abs(asum-bsum)
        return

    DFS(n+1, A+[n], B)
    DFS(n+1, A, B+[n])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 999999999
    DFS(0, [], [])
    print(f'#{tc} {ans}')