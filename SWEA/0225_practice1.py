# 주석처리 된 부분은 원형 큐일 때

class MyQueue:
    def __init__(self):
        self.N = 100
        self.queue = [0]*self.N
        self.front = -1
        self.rear = -1
        # self.front = 0
        # self.rear = 0

    def enqueue(self, item):
        if self.is_full():
            return 'Queue_full'
        else:
            self.rear += 1
            # self.rear = (self.rear + 1) % self.N
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            return 'Queue_empty'
        else:
            self.front += 1
            # self.front = (self.front + 1) % self.N
            return self.queue[self.front]

    def is_full(self):
        return self.rear == len(self.queue)-1
        # return self.front == (self.rear+1)%len(self.queue)

    def is_empty(self):
        return self.front == self.rear

    def qpeek(self):
        if self.is_empty():
            return 'Queue_empty'
        else:
            return self.queue[self.front+1]


myqueue = MyQueue()
myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
print(myqueue.dequeue())
print(myqueue.dequeue())
print(myqueue.dequeue())
