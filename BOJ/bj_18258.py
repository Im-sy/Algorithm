class myqueue():
    def __init__(self):
        global N
        self.queue = [0]*N
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if self.isfull():
            print('Queue full')
        else:
            self.rear += 1
            self.queue[self.rear] = item

    def dequeue(self):
        if self.isempty():
            return -1
        else:
            self.front += 1
            return self.queue[self.front]

    def mysize(self):
        return self.rear - self.front

    def isempty(self):
        if self.front == self.rear:
            return 1
        else:
            return 0

    def isfull(self):
        return self.rear == N-1

    def myfront(self):
        if self.isempty():
            return -1
        else:
            return self.queue[self.front+1]

    def myback(self):
        if self.isempty():
            return -1
        else:
            return self.queue[self.rear]

import sys
# N = int(input())
N = int(sys.stdin.readline())
new_queue = myqueue()
for _ in range(N):
    # result = input().split()
    result = sys.stdin.readline().split()
    a = result[0]
    if a == 'push':
        new_queue.enqueue(int(result[1]))
    elif a == 'pop':
        print(new_queue.dequeue())
    elif a == 'size':
        print(new_queue.mysize())
    elif a == 'empty':
        print(new_queue.isempty())
    elif a == 'front':
        print(new_queue.myfront())
    elif a == 'back':
        print(new_queue.myback())