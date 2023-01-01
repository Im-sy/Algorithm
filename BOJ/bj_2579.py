# 왜 런타임 에러?? IndexError??

import sys
N = int(sys.stdin.readline())
arr = [0] + [int(sys.stdin.readline()) for _ in range(N)]
ans = [0]*(N+1)
ans[1] = arr[1]
# N==1인경우 조심하자..
if N >= 2:
    ans[2] = ans[1]+arr[2]
# print(arr)
# 2 + 1 or 1 + 2
# ans[3] = 0 -> 2 -> 3 or 1 -> 3
# ans[4] = 1 -> 3 -> 4 or 2 -> 4
# ans[n] = n-3 -> n-1 -> n or n-2 -> n
for i in range(3, N+1):
    ans[i] = max(ans[i-3]+arr[i-1], ans[i-2]) + arr[i]
print(ans[N])