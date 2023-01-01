import sys
sys.stdin = open('swea_1225.txt')

class MyQueue:
    def __init__(self):
        self.N = 9
        self.queue = [0]*self.N
        self.front = 0
        self.rear = 0

    def enqueue(self, item):
        if self.is_full():
            print('Queue_full')
            return
        else:
            self.rear = (self.rear + 1) % self.N
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print('Queue_empty')
            return
        else:
            self.front = (self.front + 1) % self.N
            return self.queue[self.front]

    def is_full(self):
        return self.front == (self.rear+1)%len(self.queue)

    def is_empty(self):
        return self.front == self.rear

    def qpeek(self):
        if self.is_empty():
            print('Queue_empty')
            return
        else:
            return self.queue[(self.front+1)%self.N]

    def __str__(self):
        result = []
        # print(self.front, self.rear)
        i = self.front + 1
        while True:
            if i>8:
                i = 0
            if i == self.rear:
                break
            result.append(self.queue[i])
            i += 1
        result.append(self.queue[self.rear])
        return ' '.join(map(str, result))

for _ in range(10):
    tc = int(input())
    password = MyQueue()
    arr = list(map(int, input().split()))
    for x in arr:
        password.enqueue(x)
    diff = 1
    # print(password)
    # print(password.rear)
    while password.queue[password.rear] != 0:
        if diff == 6:
            diff = 1
        if password.qpeek() - diff <= 0:
            password.dequeue()
            password.enqueue(0)
            break
        password.enqueue(password.dequeue() - diff)
        diff += 1
    print(f'#{tc} {password}')