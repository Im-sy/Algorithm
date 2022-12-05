from itertools import combinations

prime = [1] * (1000000 + 1)
prime[0] = 0
prime[1] = 0
m = int(1000000 ** 0.5)
for i in range(2, m + 1):
    if prime[i]:
        for j in range(2 * i, 1000000 + 1, i):
            prime[j] = 0

while True:
    n = int(input())
    if n == 0:
        break

    # prime_list = []
    # for i in range(n+1):
    #     if prime[i]:
    #         prime_list.append(i)
    # tmp = []
    # for comb in combinations(prime_list, 2):
    #     if sum(comb) == n:
    #         tmp.append(comb)
    # if not tmp:
    #     print("Goldbach's conjecture is wrong.")
    # else:
    #     minus = 0
    #     ans = (0, 0)
    #     for t in tmp:
    #         a, b = t
    #         if minus < b-a:
    #             minus = b-a
    #             ans = (a, b)
    #     print("{} = {} + {}".format(n, ans[0], ans[1]))

    for i in range(2, 1000000+1):
        if prime[i] and prime[n-i]:
            print("{} = {} + {}".format(n, i, n-i))
            break