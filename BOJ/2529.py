import sys
input = sys.stdin.readline

k = int(input())
arr = list(input().split())

MIN = float('INF')
MAX = float('-INF')

v = [0]*10

def check(a, b, cal):
    a = int(a)
    if cal == '<':
        return a<b
    else:
        return a>b

def solve(level, tmp):
    global MIN, MAX
    if level == k+1:
        MIN = min(MIN, int(tmp))
        MAX = max(MAX, int(tmp))
        return
    for i in range(10):
        if level == 0 or not v[i] and check(tmp[-1], i, arr[level-1]):
            v[i] = 1
            solve(level+1, tmp+str(i))
            v[i] = 0

solve(0, '')
print(str(MAX))
if len(str(MIN)) < k+1:
    print('0'+str(MIN))
else:
    print(str(MIN))