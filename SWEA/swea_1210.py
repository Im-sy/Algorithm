import sys
sys.stdin = open('swea_1210.txt', 'r')
for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    r = 99
    for i in range(100):
        if arr[99][i] == 2:
            c = i
            break
    while r:
        if c>0 and arr[r][c-1]: # 왼쪽에 길 있으면
            while c>0 and arr[r][c-1]:
                c -= 1
        elif c<99 and arr[r][c+1]: # 오른쪽에 길 있으면
            while c<99 and arr[r][c+1]:
                c += 1
        r -= 1
    print(f'#{tc} {c}')


# 델타 방향 사용 but 효율은 그닥..
#
# dr = [-1, 0, 0] # 상 좌 우
# dc = [0, -1, 1]
# for _ in range(10):
#     tc = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]
#     r = 99
#     for i in range(100):
#         if arr[99][i] == 2:
#             c = i
#             break
#     dir = 0
#     while True:
#         if r == 0:
#             break
#         if c>0 and arr[r][c-1]:
#             dir = 1
#             while c>0 and arr[r][c-1]:
#                 r += dr[dir]
#                 c += dc[dir]
#         elif c<99 and arr[r][c+1]:
#             dir = 2
#             while c<99 and arr[r][c+1]:
#                 r += dr[dir]
#                 c += dc[dir]
#         dir = 0
#         r += dr[dir]
#         c += dc[dir]
#     print(f'#{tc} {c}')