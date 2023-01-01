T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    stack = []
    for x in arr:
        if x.isdecimal():
            stack.append(int(x))
        else:
            if x == '.':
                if len(stack)==1:
                    ans = stack.pop()
                else:
                    ans = 'error'
                break
            if len(stack)>1:
                a = stack.pop()
                b = stack.pop()
                if x == '*':
                    stack.append(b*a) # 계산할 때 a, b 순서 중요!!!! b가 먼저임
                elif x == '/':
                    stack.append(b//a)
                elif x == '+':
                    stack.append(b+a)
                elif x == '-':
                    stack.append(b-a)
            else:
                ans = 'error'
                break
    print(f'#{tc} {ans}')