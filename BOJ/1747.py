N = int(input())

prime = [1]*10000000
prime[0] = 0
prime[1] = 0
m = int(10000000 ** 0.5)
for i in range(2, m + 1):
    if prime[i]:
        for j in range(2 * i, 10000000, i):
            prime[j] = 0

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

while True:
    if isPrime(N) and str(N)==str(N)[::-1]:
        print(N)
        break
    N += 1