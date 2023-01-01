A, B, C = map(int, input().split())
def solve(a, b):
    if b == 1:
        return a%C
    tmp = solve(a, b//2)
    if b%2:
        return tmp*tmp*a%C
    else:
        return tmp*tmp%C
print(solve(A, B))