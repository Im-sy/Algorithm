while True:
    n = int(input())
    if n == 0:
        break
    prime = [1]*(2*n+1)
    prime[0] = 0
    prime[1] = 0
    m = int((2*n)**0.5)
    for i in range(2, m+1):
        if prime[i]:
            for j in range(2*i, 2*n+1, i):
                prime[j] = 0
    cnt = 0
    for i in range(n+1, n*2+1):
        if prime[i]:
            cnt += 1
    print(cnt)