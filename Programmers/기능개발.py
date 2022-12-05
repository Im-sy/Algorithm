from collections import deque
progresses = deque([95, 90, 99, 99, 80, 99])
speeds = deque([1, 1, 1, 1, 1, 1])

q = deque([])
# 7 3 9
# 5 10 1 1 20 1

# while progresses:
#     progress = progresses.popleft()
#     speed = speeds.popleft()
#     cnt = 0
#     while progress < 100:
#         progress += speed
#         cnt += 1
#     q.append(cnt)
# print(q)

import math
for i, j in zip(progresses, speeds):
    q.append(math.ceil((100-i)/j))
print(q)

ans = []
tmp = 1
feat = q.popleft()
while q:
    if feat < q[0]:
        ans.append(tmp)
        tmp = 1
        feat = q.popleft()
    else:
        tmp += 1
        q.popleft()
ans.append(tmp)
print(ans)