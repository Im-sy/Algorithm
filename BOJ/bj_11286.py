import sys
N = int(sys.stdin.readline())
tree = [0]*(N+1)
last = 0

def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c//2
    while p>=1 and abs(tree[p]) >= abs(tree[c]):
        if abs(tree[p]) == abs(tree[c]):
            if tree[p] > tree[c]:
                tree[p], tree[c] = tree[c], tree[p]
        else:
            tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

def deq():
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    last -= 1
    p = 1
    c = p * 2
    while c<=last:
        if c+1<=last and abs(tree[c]) > abs(tree[c+1]):
            c += 1
        if abs(tree[p]) >= abs(tree[c]):
            if abs(tree[p]) == abs(tree[c]):
                if tree[p] > tree[c]:
                    tree[p], tree[c] = tree[c], tree[p]
            else:
                tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p*2
        else:
            break
    return tmp

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if tree[last]:
            print(deq())
        else:
            print(0)
    else:
        enq(x)

import heapq
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))