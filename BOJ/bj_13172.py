import sys
input = sys.stdin.readline

M = int(input())
dices = []
mod = 1000000007
ans = 0

def pow(a, b):
    if b == 1:
        return a % mod
    tmp = pow(a, b // 2)
    if b%2:
        return a*tmp*tmp%mod
    else:
        return tmp*tmp%mod

for _ in range(M):
    Ni, Si = map(int, input().split())
    ans += Si*pow(Ni, mod-2)%mod
print(ans%mod)