n = int(input())
stack = []
result = []
i = 1
for _ in range(n):
    num = int(input())
    while i <= num:
        stack.append(i)
        result.append('+')
        i += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        break
else:
    for x in result:
        print(x)