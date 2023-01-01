import sys
sys.stdin = open('swea_1224.txt')

isp = {'*':2, '+':1, '(':0}
icp = {'*':2, '+':1, '(':3}
for tc in range(1, 11):
    N = int(input())
    string = input()
    stack = []
    path = []
    for s in string:
        if s in '0123456789':
            path.append(s)
        elif s in '*+(':
            if not stack:
                stack.append(s)
            else:
                # 내가 크면 그냥 들어감, 나보다 큰 게 있으면 다 빼고 들어감
                if isp[stack[-1]] >= icp[s]:
                    while stack and isp[stack[-1]] >= icp[s]:
                        path.append(stack.pop())
                stack.append(s)
        else:
            while stack[-1] != '(':
                path.append(stack.pop())
            stack.pop() # '('까지 pop!
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
                stack.append(b*a)
            else:
                stack.append(b+a)
    print(f'#{tc} {stack.pop()}')