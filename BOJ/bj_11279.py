# 완전 이진트리, 루트노드보다 크냐 작냐에 따라 최대 힙, 최소 힙
# 완전 이진트리라 자식//2=부모, 부모*2=자식

# 1. tree 배열 만들어두고 사용 (시간초과)
# 최대 힙에 입력
def enq(n):
    global last
    last += 1
    # tree의 마지막에 입력 후
    # 부모노드와 자식노드 간 크기를 비교해가며 교환
    tree[last] = n
    c = last
    p = c//2
    while p>=1 and tree[p] < tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

# 최대 힙에서 가장 큰 값(루트노드) 출력 및 삭제
def deq():
    global last
    # 가장 큰 값 = 루트노드 (반환해서 출력용으로 저장)
    tmp = tree[1]
    # tree의 마지막 값을 루트노드로 가져온 후 마지막 값은 삭제
    tree[1] = tree[last]
    tree[last] = 0
    last -= 1
    # 자식노드와 부모노드 간 크기를 비교해가며 교환
    p = 1
    c = p*2 # 왼쪽 자식 노드
    while c<=last:
        # 오른쪽 자식 노드가 있고 왼쪽자식보다 크다면 오른쪽 자식 사용
        if c+1<=last and tree[c] < tree[c+1]:
            c += 1
        if tree[p] < tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p*2
        else:
            break
    return tmp


# import sys
# N = int(sys.stdin.readline())
# tree = [0]*(N+1)
# last = 0
# for _ in range(N):
#     x = int(sys.stdin.readline())
#     if x == 0:
#         # 만약 tree가 모두 0으로 이루어져있다면 0 출력
#         for t in tree:
#             if t != 0:
#                 break
#         else:
#             print('0')
#             continue
#         print(deq())
#     else:
#         enq(x)
    # print(x, tree)


# 2. heapq 모듈 사용한 방법
# import sys
# import heapq
# N = int(sys.stdin.readline())
# q = []
# for _ in range(N):
#     x = int(sys.stdin.readline())
#     if x == 0:
#         if len(q) == 0:
#             print(0)
#         else:
#             print(abs(heapq.heappop(q)))
#     else:
#         heapq.heappush(q, -x)


# 3. tree(h)를 스택처럼 사용하기
def insert(n):
    global last
    h.append(n)
    last += 1
    c = last
    p = c//2
    while p>=1 and h[p] < h[c]:
        h[p], h[c] = h[c], h[p]
        c = p
        p = c//2

def delete():
    global last
    print(h[1])
    h[1] = h[last]
    last -= 1
    h.pop()
    p = 1
    c = p * 2
    while c <= last:
        if c + 1 <= last and h[c] < h[c + 1]:
            c += 1
        if h[p] < h[c]:
            h[p], h[c] = h[c], h[p]
            p = c
            c = p * 2
        else:
            break

import sys
N = int(sys.stdin.readline())
h = [0]
# last값 사용하려고 h에 0 미리 넣어놨는데
# h = [] 하고 last가 아니라 len(h)-1 사용해도 무관할듯
last = 0
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(h) == 1:
            print(0)
        else:
            delete()
    else:
        insert(x)