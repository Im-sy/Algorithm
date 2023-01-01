N = int(input())
import math
fact = str(math.factorial(N))
cnt = 0
for i in range(len(fact)-1, -1, -1):
    if fact[i] == '0':
        cnt += 1
    else:
        break
print(cnt)