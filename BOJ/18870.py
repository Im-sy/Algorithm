import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
X_sort = sorted(list(set(X)))
X_dict = {}

tmp = 0
for x in X_sort:
    X_dict[x] = tmp
    tmp += 1

for i in range(N):
    X[i] = X_dict[X[i]]
# print(X_dict)
print(*X)