T = int(input())
def check():
    stack = []
    for x in arr:
        if x == '(' or x == '{':
            stack.append(x)
        elif x == ')' or x == '}':
            if not stack:
                return 0
            elif (x==')' and stack[-1]=='(') or (x=='}' and stack[-1]=='{'):
                stack.pop()
            elif (x==')' and stack[-1]!='(') or (x=='}' and stack[-1]!='{'):
                return 0
    if stack:
        return 0
    else:
        return 1

for tc in range(1, T+1):
    arr = input()
    print(f'#{tc} {check()}')