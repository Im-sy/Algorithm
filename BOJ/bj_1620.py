import sys
N, M = map(int, sys.stdin.readline().split())
dict = [sys.stdin.readline().strip() for _ in range(N)]
# print(dict)
for _ in range(M):
    find = sys.stdin.readline().strip()
    if find.isdecimal():
        print(dict[int(find)-1])
    else:
        print(dict.index(find)+1)