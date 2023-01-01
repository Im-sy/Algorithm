import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    p = list(input().strip())
    n = int(input())
    numbers = input()
    if n == 0:
        numbers = []
    else:
        numbers = deque(list(map(int, numbers.strip()[1:-1].split(','))))
    flag = 1
    for func in p:
        if func == 'R':
            flag *= -1
        else:
            if numbers:
                if flag == 1:
                    numbers.popleft()
                else:
                    numbers.pop()
            else:
                print('error')
                break
    else:
        if flag == -1:
            numbers = reversed(numbers)
        print(f'[{",".join(list(map(str, numbers)))}]')
