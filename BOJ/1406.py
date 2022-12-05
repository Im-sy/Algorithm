import sys
input = sys.stdin.readline

arr = list(input().strip())
N = len(arr)
M = int(input())
cursor = N

# for _ in range(M):
#     t = input().split()
#     if t[0] == 'L':
#         if cursor > 0:
#             cursor -= 1
#     elif t[0] == 'D':
#         if cursor < len(arr):
#             cursor += 1
#     elif t[0] == 'B':
#         if cursor > 0:
#             arr.pop(cursor-1)
#             cursor -= 1
#     else:
#         arr.insert(cursor, t[1])
#         cursor += 1
#     # print(arr, cursor)
# print(''.join(arr))

arr_tmp = []
for _ in range(M):
    t = input().split()
    if t[0] == 'L':
        if arr:
            arr_tmp.append(arr.pop())
    elif t[0] == 'D':
        if arr_tmp:
            arr.append(arr_tmp.pop())
    elif t[0] == 'B':
        if arr:
            arr.pop()
    else:
        arr.append(t[1])

arr.extend(reversed(arr_tmp))
print(''.join(arr))