def check(S):
    stack = []
    for s in S:
        if s == '(':
            # push
            stack.append(s)
        elif s == ')':
            # pop
            if stack:
                stack.pop()
            else:
                return False
    # stack 남으면 안됨
    # stack 비어있으면 ok
    if stack:
        return False
    else:
        return True


S = input()
print(check(S))