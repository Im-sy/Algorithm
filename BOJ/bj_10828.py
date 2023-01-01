class mystack():
    def __init__(self):
        self.stack = []

    def mypush(self, item):
        self.stack.append(item)

    def mypop(self):
        if self.isempty():
            return -1
        else:
            return self.stack.pop()

    def mysize(self):
        return len(self.stack)

    def isempty(self):
        if self.stack:
            return 0
        else:
            return 1

    def mytop(self):
        if self.isempty():
            return -1
        else:
            return self.stack[-1]

import sys
# N = int(input())
N = int(sys.stdin.readline())
new_stack = mystack()
for _ in range(N):
    # result = input().split()
    result = sys.stdin.readline().split()
    a = result[0]
    if a == 'push':
        new_stack.mypush(int(result[1]))
    elif a == 'pop':
        print(new_stack.mypop())
    elif a == 'size':
        print(new_stack.mysize())
    elif a == 'empty':
        print(new_stack.isempty())
    elif a == 'top':
        print(new_stack.mytop())
    # print(new_stack.stack)