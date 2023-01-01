import sys
N = int(input())
M = int(input())
S = sys.stdin.readline().strip()
# io = 'IO'*N + 'I'
# cnt = 0
# for i in range(M-(2*N+1)):
#     if S[i] == 'I':
#         if S[i:i+(2*N+1)] == io:
#             cnt += 1

cnt = 0
pattern = 0
i = 1
while i < M-1:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        pattern += 1
        if pattern == N:
            pattern -= 1
            cnt += 1
        i += 2
    else:
        pattern = 0
        i += 1

print(cnt)