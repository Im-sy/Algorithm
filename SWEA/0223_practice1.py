# S = input()
# stack = []
# for s in S:
#     if s.isdecimal():
#         print(s, end=' ')
#     else:
#         stack.append(s)
# while stack:
#     print(stack.pop(), end=' ')

# 후위 연산자 계산 (교수님)
isp = {'*':2, '/':2, '+':1, '-':1, '(':0} # stack 내부 우선순위
icp = {'*':2, '/':2, '+':1, '-':1, '(':3} # stack 외부 우선순위
data = '2+3*4/5'
stack = []
for i in range(len(data)):
    # 1. 피연산자는 그냥 출력
    if data[i] in '0123456789':
        print(data[i], end='')
    # 2. 연산자는 우선순위에 따라 stack에 push / pop 후에 push
    elif data[i] in '*/+-(':
        if not stack:
            stack.append(data[i])
        else:
            # 내가 크면 그냥 들어감, 나보다 큰 게 있으면 다 빼고 들어감
            if isp[stack[-1]] >= icp[data[i]]:
                while stack and isp[stack[-1]] >= icp[data[i]]:
                    print(stack.pop(), end='')
            stack.append(data[i])
    # 3. 닫는 괄호는 여는 괄호가 나올 때까지 pop
    else:
        while stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
# 남아있는 연산자 모두 출력
while stack:
    print(stack.pop(), end='')