T = int(input())

prime = [1] * (10000 + 1)
prime[0] = 0
prime[1] = 0
m = int(10000 ** 0.5)
for i in range(2, m + 1):
    if prime[i]:
        for j in range(2 * i, 10000 + 1, i):
            prime[j] = 0

for _ in range(T):
    n = int(input())
    for i in range(n//2, -1, -1):
        if prime[i] and prime[n-i]:
            print(i, n-i)
            break