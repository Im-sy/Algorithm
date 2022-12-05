from collections import deque

q1 = deque([3, 2, 7, 2])
q2 = deque([4, 6, 5, 1])
m = (sum(q1) + sum(q2))//2

# 11 28
q1_sum = sum(q1)
q2_sum = sum(q2)
ans = 0
while q1 and q2:
    if q1_sum < m:
        q1_sum += q2[0]
        # q2_sum -= q2[0]
        q1.append(q2.popleft())
        ans += 1
    elif q1_sum > m:
        q1_sum -= q1[0]
        # q2_sum += q1[0]
        # q2.append(q1.popleft())
        ans += 1
    else:
        print(ans)
        break
else:
    print(-1)