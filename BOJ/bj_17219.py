import sys
N, M = map(int, sys.stdin.readline().split())
# pwd = [list(sys.stdin.readline().split()) for _ in range(N)]
# find = [sys.stdin.readline().strip() for _ in range(M)]
# for y in find:
#     for x in pwd:
#         if x[0]==y:
#             print(x[1])

pwd = {}
for _ in range(N):
    ad, p = sys.stdin.readline().split()
    pwd[ad] = p
for _ in range(M):
    print(pwd[sys.stdin.readline().strip()])