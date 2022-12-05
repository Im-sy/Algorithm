s = input()
stack = []

for x in s:
    if x == '(':
        stack.append(x)
    else:
        while stack and stack[-1] != '(':
            stack.pop()
        if stack:
            stack.pop()
        else:
            print('false')
            break
else:
    if stack:
        print('false')
    else:
        print('true')