class MyStack:
    def __init__(self):
        self.stack = [0]*10
        self.top = -1
        self.size = 10

    # item을 마지막 요소 뒤에 추가
    def push(self, item):
        if self.top == self.size - 1:
            print('Full')
        else:
            self.top += 1
            self.stack[self.top] = item

    # 마지막 요소 반환 후 삭제
    def pop(self):
        if self.top == -1:
            print('Empty')
        else:
            self.top -= 1
            return self.stack[self.top + 1]

    # 마지막 요소 반환
    def peek(self):
        return self.stack[self.top + 1]

    # stack이 비어있는지 확인
    def isEmpty(self):
        if self.top == -1:
            return True

stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())