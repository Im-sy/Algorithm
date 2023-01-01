import sys
T = int(input())
for _ in range(T):
    N = int(input())
    clothes = {}
    for _ in range(N):
        c, t = sys.stdin.readline().split()
        if t in clothes:
            clothes[t] += 1
        else:
            clothes[t] = 1
    ans = 1
    for v in clothes.values():
        ans *= (v+1)
    print(ans-1)

# 1차 - 자외선