# N = int(input())
# card = [i for i in range(1, N+1)]
# while len(card)>1:
#     card.pop(0)
#     card.append(card.pop(0))
# print(*card)

class myqueue():
    def __init__(self):
        global N
        self.queue = [0]*2*N
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
        return self.rear == 2*N-1

    def myback(self):
        if self.isempty():
            return -1
        else:
            return self.queue[self.rear]

N = int(input())
card = myqueue()
for i in range(1, N+1):
    card.enqueue(i)
while card.mysize() > 1:
    card.dequeue()
    card.enqueue(card.dequeue())
print(card.myback())