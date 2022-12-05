import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

stack = []
ans = [0]*N
for i in range(N):
    while stack:
        idx, height = stack[-1]
        if height > arr[i]:
            ans[i] = idx + 1
            break
        else:
            stack.pop()
    stack.append((i, arr[i]))
    # print(stack)
print(*ans)