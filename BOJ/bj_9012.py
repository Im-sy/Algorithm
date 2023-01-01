def check():
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return 'NO'
            else:
                return 'NO'
    if stack:
        return 'NO'
    else:
        return 'YES'

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    string = sys.stdin.readline()
    print(check())