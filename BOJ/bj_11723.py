import sys
input = sys.stdin.readline
M = int(input())
ans = set()
for _ in range(M):
    check = input().split()
    a = check[0]
    if len(check) == 1:
        if a == 'all':
            ans = set(range(1, 21))
        else:
            ans = set()
    else:
        x = int(check[1])
        if a == 'add':
            ans.add(x)
        elif a == 'remove':
            ans.discard(x)
        elif a == 'check':
            if x in ans:
                print(1)
            else:
                print(0)
        elif a == 'toggle':
            if x in ans:
                ans.discard(x)
            else:
                ans.add(x)



# ans = []
# for _ in range(M):
#     check = input().split()
#     a = check[0]
#     if a == 'add':
#         if check[1] not in ans:
#             ans.append(check[1])
#     elif a == 'remove':
#         if check[1] in ans:
#             ans.remove(check[1])
#     elif a == 'check':
#         if check[1] in ans:
#             print(1)
#         else:
#             print(0)
#     elif a == 'toggle':
#         if check[1] not in ans:
#             ans.append(check[1])
#         else:
#             ans.remove(check[1])
#     elif a == 'all':
#         ans = list(map(str, range(1, 21)))
#     else:
#         ans = []