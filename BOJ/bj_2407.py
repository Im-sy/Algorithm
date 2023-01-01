n, m = map(int, input().split())
ans = 1
for i in range(n, n-m, -1):
    ans *= i
tmp = 1
for j in range(1, m+1):
    tmp *= j
print(ans//tmp)