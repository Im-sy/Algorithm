from collections import deque


def solution(x, y, n):
    v = [0]*1000001
    q = deque([x])
    v[x] = 1
    while q:
        f = q.popleft()
        if f+n<=1000000 and v[f+n]==0:
            v[f+n] = v[f] + 1
            q.append(f+n)
        if f*2<=1000000 and v[f*2]==0:
            v[f*2] = v[f] + 1
            q.append(f*2)
        if f*3<=1000000 and v[f*3]==0:
            v[f*3] = v[f] + 1
            q.append(f*3)
    return v[y]-1


print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))