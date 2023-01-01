import sys
N, M = map(int, sys.stdin.readline().split())
nohear = [sys.stdin.readline().strip() for _ in range(N)]
nosee = [sys.stdin.readline().strip() for _ in range(M)]
# ans = []
# for x in nohear:
#     if x in nosee:
#         ans.append(x)
# print(len(ans))
# print(sorted(ans))

ans = sorted(list(set(nohear)&set(nosee)))
print(len(ans))
for x in ans:
    print(x)