import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
snake = deque([list(input().split()) for _ in range(L)])

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
time = 0
path = deque([(0, 0)])
t, d = snake.popleft()
idx = 0

while 0<=path[-1][0]+dir[idx][0]<N and 0<=path[-1][1]+dir[idx][1]<N:
    r = path[-1][0]+dir[idx][0]
    c = path[-1][1]+dir[idx][1]
    if (r, c) not in path:
        path.append((r, c))
        time += 1
        if [r+1, c+1] in apple:
            apple.remove([r+1, c+1])
        else:
            path.popleft()
        if time == int(t):
            if d == 'L':
                idx = (idx-1) % 4
            elif d == 'D':
                idx = (idx+1) % 4
            if snake:
                t, d = snake.popleft()
    else:
        break

print(time+1)