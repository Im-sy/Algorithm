s = input()

stackA = []
stackB = []
ans = 0
tmp = 1
for i, x in enumerate(s):
    if x == '(':
        stackA.append(x)
        tmp *= 2
    elif x == '[':
        stackB.append(x)
        tmp *= 3
    elif x == ')':
        if stackA:
            if s[i-1] == '(':
                ans += tmp
            stackA.pop()
            tmp //= 2
        else:
            ans = 0
            break
    else:
        if stackB:
            if s[i-1] == '[':
                ans += tmp
            stackB.pop()
            tmp //= 3
        else:
            ans = 0
            break
    # print(stackA, stackB)
if stackA or stackB:
    print(0)
else:
    print(ans)