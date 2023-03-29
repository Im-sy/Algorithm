from collections import deque


def solution(order):
    answer = []
    order = deque(order)
    stack = []
    box = deque(list(range(1, len(order)+1)))
    while order:
        num = order.popleft()
        # print(num)
        # print(f'box: {box}')
        # print(f'stack: {stack}')
        # print(f'answer: {answer}')
        while box and box[0] <= num:
            stack.append(box.popleft())
        if stack[-1] == num:
            answer.append(stack.pop())
        else:
            break
    return len(answer)


print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))
