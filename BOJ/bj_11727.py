N = int(input())
ans = [0]*(N+1)
ans[0] = 1
ans[1] = 1
for i in range(2, N+1):
    ans[i] = (ans[i-2]*2 + ans[i-1])%10007
print(ans[N])