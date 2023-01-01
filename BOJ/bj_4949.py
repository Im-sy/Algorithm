import sys
while True:
    string = sys.stdin.readline()
    if string == '.\n':
        break
    stack = []
    for s in string:
        if s in '([':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s)
                break
    if stack:
        print('no')
    else:
        print('yes')
