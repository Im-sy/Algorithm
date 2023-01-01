import sys
import heapq
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k = int(input())
    mheap = []
    Mheap = []
    visited = [0]*1000001
    for i in range(k):
        read = input().split()
        if read[0] == 'I':
            heapq.heappush(mheap, (int(read[1]), i))
            heapq.heappush(Mheap, (-int(read[1]), i))
            visited[i] = 1
        elif read[1] == '1':
            while Mheap and not visited[Mheap[0][1]]:
                heapq.heappop(Mheap)
            if Mheap:
                visited[Mheap[0][1]] = 0
                heapq.heappop(Mheap)
        else:
            while mheap and not visited[mheap[0][1]]:
                heapq.heappop(mheap)
            if mheap:
                visited[mheap[0][1]] = 0
                heapq.heappop(mheap)
    while Mheap and not visited[Mheap[0][1]]:
        heapq.heappop(Mheap)
    while mheap and not visited[mheap[0][1]]:
        heapq.heappop(mheap)
    if mheap and Mheap:
        print(-Mheap[0][0], mheap[0][0])
    else:
        print('EMPTY')