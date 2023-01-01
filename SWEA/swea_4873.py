T = int(input())
for tc in range(1, T+1):
    string = input()
    stack = []
    for i in range(len(string)):
        if not stack:
            stack.append(string[i])
            continue
        if string[i] != stack[-1]:
            stack.append(string[i])
        elif string[i] == stack[-1]:
            stack.pop()
    print(f'#{tc} {len(stack)}')