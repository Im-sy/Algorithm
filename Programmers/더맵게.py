import heapq

scoville = [1, 2, 3]
K = 11

heapq.heapify(scoville)
ans = 0
while len(scoville)>1:
    if scoville[0] >= K:
        break
    heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
    ans += 1
else:
    if scoville[0] >= K:
        pass
    else:
        ans = -1

print(ans)