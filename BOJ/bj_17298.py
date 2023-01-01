N = int(input())
arr = list(map(int, input().split()))
result = [-1]*N
stack = [0]
for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack[-1]] = arr[i]
        stack.pop()
    stack.append(i)
print(*result)