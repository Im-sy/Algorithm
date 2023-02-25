from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    q = deque([0]*bridge_length)
    total = 0
    while trucks:
        total -= q.popleft()
        if total + trucks[0] > weight:
            q.append(0)
        else:
            w = trucks.popleft()
            total += w
            q.append(w)
        answer += 1
    return answer + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))