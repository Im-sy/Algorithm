arrs = input()
oper = {'+':1, '-':1, '*':2, '/':2, '(':0}
ans = []
stack = []
for x in arrs:
    if 'A' <= x <= 'Z':
        ans.append(x)
    elif x == '(':
        stack.append(x)
    elif x == ')':
        while stack and stack[-1] != '(':
            ans.append(stack.pop())
        stack.pop()
    else:
        while stack and oper[x] <= oper[stack[-1]]:
            ans.append(stack.pop())
        stack.append(x)
while stack:
    ans.append(stack.pop())

print(''.join(map(str, ans)))
