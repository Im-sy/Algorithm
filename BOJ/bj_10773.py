import sys
K = int(sys.stdin.readline())
arr = []
for _ in range(K):
    n = int(sys.stdin.readline())
    if n :
        arr.append(n)
    else:
        arr.pop()
print(sum(arr))
