import sys
sys.stdin = open('swea_1223.txt')
isp = {'*':2, '+':1}
for tc in range(1, 11):
    N = int(input())
    string = input()
    stack = []
    path = []
    for s in string:
        if s in '0123456789':
            path.append(s)
        else:
            if not stack:
                stack.append(s)
            else:
                if isp[stack[-1]] >= isp[s]:
                    while stack and isp[stack[-1]] >= isp[s]:
                        path.append(stack.pop())
                stack.append(s)
    while stack:
        path.append(stack.pop())
    stack = []
    for x in path:
        if x in '0123456789':
            stack.append(x)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if x == '*':
                stack.append(a*b)
            else:
                stack.append(a+b)
    print(f'#{tc} {stack.pop()}')