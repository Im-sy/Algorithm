import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())
arrs = sorted(list(input().split()))

for comb in combinations(arrs, L):
    a, b = 0, 0
    for x in comb:
        if x in ['a', 'e', 'i', 'o', 'u']:
            a += 1
        else:
            b += 1
    if a>=1 and b>=2:
        print(''.join(comb))